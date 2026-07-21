class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        ans = i = 0
        prev = float('-inf')   # length of previous zero-run; -inf so a lone run can't pair
        best = 0               # best combined size of two adjacent zero-runs
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            cur = j - i
            if s[i] == '1':
                ans += cur                      # count active sections
            else:
                best = max(best, prev + cur)    # merge with the previous zero-run
                prev = cur
            i = j
        return ans + best