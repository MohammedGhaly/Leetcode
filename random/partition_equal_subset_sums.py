class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        s = sum(nums) 
        if s % 2:
            return False
        t = s / 2
        dp = set()
        dp.add(0)
        
        for i in range(len(nums)):
            nextDP = set()
            
            for num in dp:
                new = num + nums[i]
                if new == t: return True
                nextDP.add(new)
                nextDP.add(num)
            # if t in nextDP : return True
            dp = nextDP
        return False
                
        
        
        
sol = Solution()
# nums = [1, 2, 5]
nums = [1, 5, 11, 5]
print(sol.canPartition(nums))
        