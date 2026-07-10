from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Sort values while keeping original indices
        arr = sorted((nums[i], i) for i in range(n))

        values = [0] * n
        pos = [0] * n
        comp = [0] * n

        comp_id = 0
        for i, (val, idx) in enumerate(arr):
            values[i] = val
            pos[idx] = i
            if i > 0 and values[i] - values[i - 1] > maxDiff:
                comp_id += 1
            comp[i] = comp_id

        # Compute farthest reachable position from each sorted index
        nxt = [0] * n
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j + 1 < n and values[j + 1] - values[i] <= maxDiff:
                j += 1
            nxt[i] = j

        # Binary lifting table
        LOG = n.bit_length()
        up = [nxt]

        for _ in range(1, LOG):
            prev = up[-1]
            curr = [0] * n
            for i in range(n):
                curr[i] = prev[prev[i]]
            up.append(curr)

        ans = []

        for u, v in queries:
            a = pos[u]
            b = pos[v]

            if comp[a] != comp[b]:
                ans.append(-1)
                continue

            if a == b:
                ans.append(0)
                continue

            if a > b:
                a, b = b, a

            cur = a
            steps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < b:
                    cur = up[k][cur]
                    steps += 1 << k

            ans.append(steps + 1)

        return ans