class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = []
        for i in range(m):
            matrix.append([0]*n)
        
        matrix[-1][-1] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if j > 0:
                    matrix[i][j-1] += matrix[i][j]
                if i > 0:
                    matrix[i-1][j] += matrix[i][j]
        
        return matrix[0][0]

sol = Solution()
res = sol.uniquePaths(1, 1)
print(res)