class Solution:
    def maxAreaOfIsland(self, grid: list[list[str]]) -> int:
        stack = []
        visited = [[False for i in range(len(grid[0]))]
                   for j in range(len(grid))]
        max_area = 0

        def add_neighbours(item: tuple):
            added_neighbours = 0
            if item[0] - 1 >= 0 and grid[item[0] - 1][item[1]] and not visited[item[0] - 1][item[1]]:
                stack.append((item[0] - 1, item[1]))  # up
                visited[item[0] - 1][item[1]] = True
                added_neighbours += 1
            if item[0] + 1 < len(grid) and grid[item[0] + 1][item[1]] and not visited[item[0] + 1][item[1]]:
                stack.append((item[0] + 1, item[1]))  # down
                added_neighbours += 1
                visited[item[0] + 1][item[1]] = True

            if item[1] - 1 >= 0 and grid[item[0]][item[1] - 1] and not visited[item[0]][item[1] - 1]:
                stack.append((item[0], item[1] - 1))  # left
                added_neighbours += 1
                visited[item[0]][item[1] - 1] = True

            if item[1] + 1 < len(grid[0]) and grid[item[0]][item[1] + 1] and not visited[item[0]][item[1] + 1]:
                stack.append((item[0], item[1] + 1))  # right
                added_neighbours += 1
                visited[item[0]][item[1] + 1] = True
            return added_neighbours

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cur_count = 0
                if grid[i][j] and not visited[i][j]:
                    stack.append((i, j))
                    visited[i][j] = True

                    cur_count = 1
                    while len(stack):
                        cur = stack.pop()
                        cur_count += add_neighbours(cur)
                    max_area = max(max_area, cur_count)

        return max_area


grid = [[1, 0, 1], [1, 0, 1], [1, 1, 1]]
print(Solution().maxAreaOfIsland(grid))
