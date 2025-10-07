from math import ceil
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        memo = set()
        for ci in range(9):
            for ri in range(9):
                if board[ri][ci] == '.':    continue
                if not (self.check_row(ri, ci, board, memo) and 
                        self.check_col(ri, ci, board, memo) and
                        self.check_box(ri, ci, board, memo)):     return False
                memo.add((ri, ci))
        return True

    def check_row(self, ri, ci, board, memo) -> bool:
        for i in range(9):
            if board[ri][i] == '.' or (ri, i) in memo:          continue
            if board[ri][i] == board[ri][ci] and ci != i:       return False
        return True

    def check_col(self, ri, ci, board, memo):
        for i in range(9):
            if board[i][ci] == '.' or (i, ci) in memo:          continue
            if board[i][ci] == board[ri][ci] and ri != i:       return False
        return True

    def check_box(self, ri, ci, board, memo) -> bool:
        start_row = (ceil((ri + 1) / 3) - 1) * 3
        start_col = (ceil((ci + 1) / 3) - 1) * 3
        
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == '.' or (i, j) in memo:          continue
                if ((board[i][j] == board[ri][ci]) and  
                    not (i == ri and j == ci)):  return False
        return True
                    

sol = Solution()

# # True
# board1 = \
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# print(sol.isValidSudoku(board1))

# # False col
# board2 = \
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# print(sol.isValidSudoku(board2))

# box   False
# board3 = \
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","5","9"]]
# print(sol.isValidSudoku(board3))

# board4 = \
# [[".",".","8",".",".",".",".",".","5"],["4",".",".",".",".","1",".",".","."],[".","9",".","8",".","4",".",".","."],[".",".",".",".",".","9",".","8","5"],["5",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","7"],[".",".",".",".",".",".","9",".","."],["7",".",".",".","9",".",".",".","2"],[".",".","9",".",".",".","3",".","."]]
# print(sol.isValidSudoku(board4))