class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total  # full rotations do nothing

        # Flatten
        flat = [grid[i][j] for i in range(m) for j in range(n)]

        # Rotate right by k
        rotated = flat[-k:] + flat[:-k] if k else flat

        # Reshape into m x n
        return [rotated[i * n:(i + 1) * n] for i in range(m)]