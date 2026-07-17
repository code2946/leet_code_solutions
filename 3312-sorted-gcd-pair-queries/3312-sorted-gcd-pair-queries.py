from bisect import bisect_right
from itertools import accumulate

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        M = max(nums)
        freq = [0] * (M + 1)
        for v in nums:
            freq[v] += 1

        # cnt[d] = how many nums are divisible by d
        cnt = [0] * (M + 1)
        for d in range(1, M + 1):
            for k in range(d, M + 1, d):
                cnt[d] += freq[k]

        # exact[d] = pairs whose gcd is exactly d
        exact = [0] * (M + 1)
        for d in range(M, 0, -1):
            c = cnt[d]
            total = c * (c - 1) // 2
            for k in range(2 * d, M + 1, d):
                total -= exact[k]
            exact[d] = total

        pref = list(accumulate(exact))          # pref[d] = # pairs with gcd <= d
        return [bisect_right(pref, q) for q in queries]