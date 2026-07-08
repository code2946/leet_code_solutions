from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        m = len(s)
        digits = [ord(c) - 48 for c in s]

        # prefix count of non-zero digits
        cnt = [0] * (m + 1)
        for i in range(m):
            cnt[i + 1] = cnt[i] + (digits[i] != 0)

        v = [d for d in digits if d != 0]
        K = len(v)

        # P[i] = concat(v[0..i-1]) mod p ; S[i] = sum(v[0..i-1])
        P = [0] * (K + 1)
        S = [0] * (K + 1)
        for i in range(K):
            P[i + 1] = (P[i] * 10 + v[i]) % MOD
            S[i + 1] = S[i] + v[i]

        pow10 = [1] * (K + 1)
        for i in range(1, K + 1):
            pow10[i] = pow10[i - 1] * 10 % MOD

        answer = []
        for l, r in queries:
            a, b = cnt[l], cnt[r + 1] - 1
            if a > b:                      # no non-zero digits
                answer.append(0)
                continue
            length = b - a + 1
            x = (P[b + 1] - P[a] * pow10[length]) % MOD
            digit_sum = S[b + 1] - S[a]
            answer.append(x * (digit_sum % MOD) % MOD)
        return answer