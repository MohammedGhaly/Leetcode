class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        visited = set()

        def backtrack(i, j, target: str) -> bool:
            if target == '':
                return True
            if ((i, j) in visited) or i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            if not board[i][j] == target[0]:
                return False

            visited.add((i, j))
            if (backtrack(i+1, j, target[1:]) or  # down
                    backtrack(i-1, j, target[1:]) or  # up
                    backtrack(i, j+1, target[1:]) or  # right
                    backtrack(i, j-1, target[1:])):  # left
                return True
            else:
                visited.remove((i, j))
                return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, word):
                    return True
        return False


print(Solution().exist(board=[['a', 'b']], word="a"))
