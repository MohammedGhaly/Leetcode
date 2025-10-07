class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
                
        z = len(nums) - 1
        if z == -1:
            return 0
        a = 0
        x =  int((a + z) / 2)
        
        while (z >= a):
            x =  int((a + z) / 2)
            if nums[x] > target:
                z = x - 1
                # x =  int((a + z) / 2)
                continue
            if nums[x] < target:
                a = x + 1
                # x =  int((a + z) / 2)
                continue
            if nums[x] == target:
                return x
            
        if nums[x] < target:
            return x + 1
        else :
            return x 
            
            
solution = Solution()

# nums = [0, 3, 7, 12, 12, 12, 12, 15, 17, 20]
# nums = [1, 3, 5, 6]
# res = solution.searchInsert(nums, 0)
l = 20
r = 100
# res = l+(r-l)//2
res = l+(r-l)//2

print(res)

                
        