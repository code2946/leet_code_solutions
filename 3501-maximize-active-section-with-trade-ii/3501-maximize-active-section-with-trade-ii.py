from typing import List
import bisect

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # run-length decomposition
        runStart, runEnd, runVal = [], [], []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runStart.append(i); runEnd.append(j - 1)
            runVal.append(1 if s[i] == '1' else 0)
            i = j
        m = len(runStart)

        # zero runs — the only things a trade touches
        zr, zStart, zEnd = [], [], []
        zeroIdxOfRun = [-1] * m
        for ri in range(m):
            if runVal[ri] == 0:
                zeroIdxOfRun[ri] = len(zr)
                zr.append(runEnd[ri] - runStart[ri] + 1)
                zStart.append(runStart[ri]); zEnd.append(runEnd[ri])
        k = len(zr)
        totalOnes = s.count('1')

        # sparse table over A[i] = zr[i] + zr[i+1]  (adjacent zero-run pair sums)
        A = [zr[i] + zr[i + 1] for i in range(k - 1)]
        LA = len(A)
        sp = [A[:]] if LA else []
        step = 1
        while step * 2 <= LA:
            prev = sp[-1]
            sp.append([max(prev[idx], prev[idx + step]) for idx in range(LA - 2 * step + 1)])
            step *= 2

        def rangeMaxA(lo, hi):                       # inclusive, 0 <= lo <= hi < LA
            e = (hi - lo + 1).bit_length() - 1
            return max(sp[e][lo], sp[e][hi - (1 << e) + 1])

        def runContaining(p):
            return bisect.bisect_right(runStart, p) - 1

        ans = []
        for l, r in queries:
            pi, qi = runContaining(l), runContaining(r)
            if pi == qi:                             # whole query inside one run -> no trade
                ans.append(totalOnes); continue

            gL = zeroIdxOfRun[pi] if runVal[pi] == 0 else zeroIdxOfRun[pi + 1]
            gR = zeroIdxOfRun[qi] if runVal[qi] == 0 else zeroIdxOfRun[qi - 1]

            if gL >= gR:                             # fewer than two zero-runs -> no pair
                ans.append(totalOnes); continue

            def eff(gi):                             # clipped length of zero-run gi inside [l, r]
                return min(zEnd[gi], r) - max(zStart[gi], l) + 1

            gain = max(eff(gL) + eff(gL + 1),        # leftmost pair (left run may be clipped)
                       eff(gR - 1) + eff(gR))        # rightmost pair (right run may be clipped)
            if gL + 1 <= gR - 2:                     # fully-interior pairs (all full length)
                gain = max(gain, rangeMaxA(gL + 1, gR - 2))
            ans.append(totalOnes + gain)
        return ans