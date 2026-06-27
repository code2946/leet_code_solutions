from typing import List
from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)

        # Handle x = 1 separately (1 squared stays 1)
        ans = 0
        if 1 in freq:
            c = freq[1]
            ans = c if c % 2 == 1 else c - 1   # use an odd count of 1s

        for x in freq:
            if x == 1:
                continue
            length = 0
            cur = x
            while freq.get(cur, 0) >= 2:        # value usable on both sides
                length += 2
                cur = cur * cur                 # square to go up the chain
            # now cur appears <2 times: it's the peak if present once,
            # otherwise drop back to the last value as the peak
            if freq.get(cur, 0) == 1:
                length += 1                     # peak used once
            else:
                length -= 1                     # over-counted, last value becomes peak
            ans = max(ans, length)

        return ans