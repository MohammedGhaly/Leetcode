class Solution:
    def missingNumber(self, nums: list[int]):
        return sum([i for i in range(len(nums)+1)]) - sum(nums)


sol = Solution()
print(sol.missingNumber([0,1, 2]))
        