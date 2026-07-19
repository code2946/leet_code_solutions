class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}  # last index of each char
        stack = []
        seen = set()

        for i, c in enumerate(s):
            if c in seen:
                continue
            # Pop larger chars that will appear again later
            while stack and stack[-1] > c and last[stack[-1]] > i:
                seen.discard(stack.pop())
            stack.append(c)
            seen.add(c)

        return "".join(stack)