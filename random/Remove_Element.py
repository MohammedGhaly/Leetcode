class Solution(object):
    def removeElement(self, nums , val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #                   p           i
        #   1   4   0   5   0   2   5   6   7   
        
        p = 0
        for i in range(0, len(nums)) :
            if not nums[i] == val:
                nums[p] = nums[i]
                p = p+1
        return p
    
    
solution = Solution()
nums = [2, 2, 2, 2]
print(solution.removeElement(nums, 2))
print(nums)
