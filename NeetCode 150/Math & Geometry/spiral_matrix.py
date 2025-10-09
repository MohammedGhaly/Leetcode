class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        
        n = len(matrix)
        m = len(matrix[0])
        
        top_limit = 0
        left_limit = -1
        bottom_limit = n
        right_limit = m
        
        i = j = 0
        
        while True:
            # move right
            if i == right_limit:
                break
            while i < right_limit:
                res.append(matrix[j][i])
                i+=1
            right_limit -=1
            i = right_limit
            j+=1
            
            # move down
            if j == bottom_limit:
                break
            while j < bottom_limit:
                res.append(matrix[j][i])
                j+=1
            bottom_limit -=1
            j = bottom_limit
            i-=1
            
            # move left
            if i == left_limit:
                break
            while i > left_limit:
                res.append(matrix[j][i])
                i-=1
            left_limit +=1
            i = left_limit
            j-=1
            # move up
            if j == top_limit:
                break
            while j > top_limit:
                res.append(matrix[j][i])
                j-=1
            top_limit +=1
            j = top_limit
            i+=1
        
        return res


sol = Solution()
matrix1 = [
          [1,2,3],
          [4,5,6],
          [7,8,9]
        ]
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix3 = [[4, 3,5]]
r = sol.spiralOrder(matrix3)
print(r)