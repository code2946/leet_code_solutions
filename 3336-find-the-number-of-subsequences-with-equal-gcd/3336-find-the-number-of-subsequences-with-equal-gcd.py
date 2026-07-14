from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        M = max(nums)
        # dp[g1][g2] = number of ways to reach these gcds (0 = empty)
        dp = [[0] * (M + 1) for _ in range(M + 1)]
        dp[0][0] = 1

        for x in nums:
            ndp = [[0] * (M + 1) for _ in range(M + 1)]
            for g1 in range(M + 1):
                row = dp[g1]
                for g2 in range(M + 1):
                    v = row[g2]
                    if v == 0:
                        continue
                    # skip x
                    ndp[g1][g2] = (ndp[g1][g2] + v) % MOD
                    # put x in seq1
                    ng1 = x if g1 == 0 else gcd(g1, x)
                    ndp[ng1][g2] = (ndp[ng1][g2] + v) % MOD
                    # put x in seq2
                    ng2 = x if g2 == 0 else gcd(g2, x)
                    ndp[g1][ng2] = (ndp[g1][ng2] + v) % MOD
            dp = ndp

        return sum(dp[g][g] for g in range(1, M + 1)) % MOD