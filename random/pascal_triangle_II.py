class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        base = [1, 1]
        
        for i in range(1, rowIndex):
            new_row = [1]
            for i in range(1, len(base)):
                new_row.append(base[i-1]+base[i])
            new_row.append(1)
            base = new_row
        return base


sol = Solution()
res = sol.getRow(5)
print(res)