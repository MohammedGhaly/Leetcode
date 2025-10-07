class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not len(nums) : return [-1, -1]
        
        res = []
        l, r = 0, len(nums)-1
        left_target = target-0.5
        right_target = target+0.5
        
        while l<=r:
            mid = (r+l)//2
            if nums[mid] < left_target:
                l=mid+1
            else:
                r=mid-1
        
        if l<len(nums) and nums[l] == target:
            res.append(l)
        else:
            res.append(-1)
        
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (r+l)//2
            if nums[mid] < right_target:
                l=mid+1
            else:
                r=mid-1
        
        if r>=0 and nums[r] == target:
            res.append(r)
        else:
            res.append(-1)
            
        return res
                



sol =Solution()
nums = [1, 2, 3]
# nums = [5, 7, 7, 8,8, 8]
print(sol.searchRange(nums, 2))
        