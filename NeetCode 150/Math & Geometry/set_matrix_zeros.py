class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = set()
        cols = set()
        # detecting the rows that need to change
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        
        # seting rows
        for row in rows:
            matrix[row] = [0 for i in range(len(matrix[row]))]
        # seting cols
        for col in cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0
                
                
             
sol = Solution()   
matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol.setZeroes(matrix)
print(matrix)