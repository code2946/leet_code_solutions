from math import gcd

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        mx = 0
        p = []
        for x in nums:
            mx = max(mx, x)
            p.append(gcd(x, mx))
        p.sort()
        i, j, ans = 0, len(p) - 1, 0
        while i < j:
            ans += gcd(p[i], p[j])
            i += 1
            j -= 1
        return ans