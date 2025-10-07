class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:  return True
        return canJump_r(nums)
    
    def canJump_r(nums : list[int], index : int) -> bool :
        if nums[index] is 0 : return False
        
        
