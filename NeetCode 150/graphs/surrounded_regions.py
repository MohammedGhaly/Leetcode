class Solution:
    def solve(self, board: list[list[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        cur_region = []

        def dfs(i: int, j: int) -> list[tuple]:
            if (i < 0 or i >= ROWS or j < 0 or j >= COLS) or ((i, j) in visited):  # out of bounds or visited
                return

            if board[i][j] == 'O':
                visited.add((i, j))
                cur_region.append((i, j))
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)

        def validate_region(cur_region):
            for i, j in cur_region:
                if i <= 0 or i >= ROWS-1 or j <= 0 or j >= COLS-1:
                    return

            for i, j in cur_region:
                board[i][j] = 'X'

        for i in range(ROWS):
            for j in range(COLS):
                if i <= 0 or i >= ROWS-1 or j <= 0 or j >= COLS-1:
                    continue
                if board[i][j] == 'O' and (i, j) not in visited:
                    dfs(i, j)
                    validate_region(cur_region)
                cur_region = []


board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "O", "X"]
]
Solution().solve(board)
print(board)
