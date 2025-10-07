class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        def dfs(i, j, value):
            if i >= rows or i < 0 or j >= cols or j < 0 or grid[i][j] == -1:
                return
            if value <= grid[i][j]:
                grid[i][j] = value
                dfs(i+1, j, value + 1)
                dfs(i-1, j, value + 1)
                dfs(i, j+1, value + 1)
                dfs(i, j-1, value + 1)

        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if not grid[row][col] == 0:
                    continue
                dfs(row, col, 0)


grid = [[-1, 0, 2147483647], [2147483647, 2147483647, -1]]

Solution().islandsAndTreasure(grid)

print(grid)
