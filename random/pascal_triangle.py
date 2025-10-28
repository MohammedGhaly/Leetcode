from math import ceil

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        base = [[1], [1,1]]
        if numRows < 3:
            return base[:numRows]
        for j in range(2, numRows):
            base.append([1])
            for i in range(1, j):
                base[-1].append(base[-2][i-1] + base[-2][i])
            base[-1].append(1)
        return base
        
    

sol = Solution()
res = sol.generate(5)
print(res)