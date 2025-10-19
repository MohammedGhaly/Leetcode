class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        results = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        pos_diags = set()  # r + c
        neg_diags = set()  # r - c

        def backtrack(r):
            if r == n:
                results.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r + c) in pos_diags or (r - c) in neg_diags:
                    continue
                
                board[r][c] = "Q"
                cols.add(c)
                pos_diags.add(r + c)
                neg_diags.add(r - c)

                backtrack(r + 1)

                board[r][c] = "."
                cols.remove(c)
                pos_diags.remove(r + c)
                neg_diags.remove(r - c)

        backtrack(0)
        return results