class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def recursive(active: list, time: int = 0):
            # base case
            if (len(active) == 0):
                for i in range(ROWS):
                    for j in range(COLS):
                        if grid[i][j] == 1:
                            return -1
                return max(time-1, 0)

            new_active = []
            for i, j in active:
                if (j+1 < COLS and grid[i][j+1] == 1):
                    grid[i][j+1] = 2     # right
                    new_active.append((i, j+1))

                if (j-1 >= 0 and grid[i][j-1] == 1):
                    grid[i][j-1] = 2     # left
                    new_active.append((i, j-1))

                if (i+1 < ROWS and grid[i+1][j] == 1):
                    grid[i+1][j] = 2     # down
                    new_active.append((i+1, j))

                if (i-1 >= 0 and grid[i-1][j] == 1):
                    grid[i-1][j] = 2     # up
                    new_active.append((i-1, j))

            return recursive(new_active, time+1)

        active = []
        # init active list with all rotten oranges
        for i in range(ROWS):
            for j in range(COLS):
                if (grid[i][j] == 2):
                    active.append((i, j))

        return recursive(active)


grid = [[0, 2]]
print(Solution().orangesRotting(grid))
