class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n
        
        for i in range(n):
            ref = nums[i]
            for j in range(i+1, n):
                if nums[j] > ref:
                    dp[j] = max(dp[j], dp[i]+1)
        return max(dp)
    

sol = Solution()
nums = [9, 1, 4, 2, 3, 3, 7]
print(sol.lengthOfLIS(nums))