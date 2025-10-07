class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        stack = []
        visited = [[False for i in range(len(grid[0]))]
                   for j in range(len(grid))]
        count = 0

        def add_neighbours(item: tuple):
            if item[0] - 1 >= 0 and grid[item[0] - 1][item[1]] == '1' and not visited[item[0] - 1][item[1]]:
                stack.append((item[0] - 1, item[1]))  # up
            if item[0] + 1 < len(grid) and grid[item[0] + 1][item[1]] == '1' and not visited[item[0] + 1][item[1]]:
                stack.append((item[0] + 1, item[1]))  # down
            if item[1] - 1 >= 0 and grid[item[0]][item[1] - 1] == '1' and not visited[item[0]][item[1] - 1]:
                stack.append((item[0], item[1] - 1))  # left
            if item[1] + 1 < len(grid[0]) and grid[item[0]][item[1] + 1] == '1' and not visited[item[0]][item[1] + 1]:
                stack.append((item[0], item[1] + 1))  # right

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    stack.append((i, j))
                    while len(stack):
                        cur = stack.pop()
                        visited[cur[0]][cur[1]] = True
                        add_neighbours(cur)

        return count


grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
print(Solution().numIslands(grid))
