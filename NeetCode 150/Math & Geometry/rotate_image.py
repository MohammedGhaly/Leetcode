class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n =len(matrix)
        levels = n // 2
        for level in range(levels):
            for i in range(level, n-level-1):
                temp = matrix[n-i-1][level]  # -> tmp = left
                matrix[n-i-1][level] = matrix[n-level-1][n-i-1]  #  -> left = bottom
                matrix[n-level-1][n-i-1] = matrix[i][n-level-1]  #  -> bottom = right
                matrix[i][n-level-1] = matrix[level][i] # -> right = top
                matrix[level][i] = temp #  -> top = left


sol = Solution()
matrix = [
    [5, 1, 2, 3, 6],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [8, 1, 2, 3, 7]
]
sol.rotate(matrix)
print(matrix)
        