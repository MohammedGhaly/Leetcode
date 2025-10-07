class Solution:
    # def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
    # ROWS, COLS = len(heights), len(heights[0])
    # p_hash_map = {}
    # a_hash_map = {}
    # # hashmap initialization
    # for index in enumerate(heights[0]):
    #     p_hash_map[(0, index)] = True
    # for index in enumerate(heights[-1]):
    #     a_hash_map[(ROWS-1, index)] = True
    # for row in heights:
    #     p_hash_map[(row, 0)] = True
    #     a_hash_map[(row, COLS-1)] = True

    # # iterate over all cells
    # for i in range(ROWS):
    #     for j in range(COLS):
    #         if p_hash_map[(i, j)] == True:
    #             a_hash_map[(i, j)] = dfs_atlantic(
    #                 i+1, j) or dfs_atlantic(i-1, j) or dfs_atlantic(i, j+1) or dfs_atlantic(i, j-1)
    #         elif p_hash_map[(i, j)] == None:
    #             dfs_pacific()

    # def dfs_atlantic():
    #     pass

    # def dfs_pacific():
    #     pass

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        matrix = [[[False, False] for cell in row] for row in heights]
        res = []
        p_starters, a_starters = [], []

        def contribute_p(i=0, j=1):
            # down
            if (i+1) < ROWS and matrix[i+1][j][0] == False and heights[i+1][j] >= heights[i][j]:
                matrix[i+1][j][0] = True
                contribute_p(i+1, j)

            # up
            if (i-1) >= 0 and matrix[i-1][j][0] == False and heights[i-1][j] >= heights[i][j]:
                matrix[i-1][j][0] = True
                contribute_p(i-1, j)

            # right
            if (j+1) < COLS and matrix[i][j+1][0] == False and heights[i][j+1] >= heights[i][j]:
                matrix[i][j+1][0] = True
                contribute_p(i, j+1)
            # left
            if (j-1) >= 0 and matrix[i][j-1][0] == False and heights[i][j-1] >= heights[i][j]:
                matrix[i][j-1][0] = True
                contribute_p(i, j-1)

        def contribute_a(i=ROWS-1, j=COLS-2):
            # up
            if (i-1) >= 0 and matrix[i-1][j][1] == False and heights[i-1][j] >= heights[i][j]:
                matrix[i-1][j][1] = True
                contribute_a(i-1, j)

            # down
            if (i+1) < ROWS and matrix[i+1][j][1] == False and heights[i+1][j] >= heights[i][j]:
                matrix[i+1][j][1] = True
                contribute_a(i+1, j)

            # left
            if (j-1) >= 0 and matrix[i][j-1][1] == False and heights[i][j-1] >= heights[i][j]:
                matrix[i][j-1][1] = True
                contribute_a(i, j-1)

            # right
            if (j+1) < COLS and matrix[i][j+1][1] == False and heights[i][j+1] >= heights[i][j]:
                matrix[i][j+1][1] = True
                contribute_a(i, j+1)

        for index, _ in enumerate(heights[0]):
            matrix[0][index][0] = True
            p_starters.append((0, index))
        for index, _ in enumerate(heights[-1]):
            a_starters.append((ROWS-1, index))
            matrix[ROWS-1][index][1] = True
        for row in range(ROWS):
            matrix[row][0][0] = True
            if row > 0:
                p_starters.append((row, 0))
            matrix[row][COLS-1][1] = True
            if not row == ROWS-1:
                a_starters.append((row, COLS-1))

        for i, j in p_starters:
            contribute_p(i, j)
        for i, j in a_starters:
            contribute_a(i, j)

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j][0] and matrix[i][j][1]:
                    res.append([i, j])

        return res


heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
    2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
# heights = [
#     [1, 2, 3],
#     [2, 2, 3],
#     [1, 2, 3],
# ]
print(Solution().pacificAtlantic(heights))
