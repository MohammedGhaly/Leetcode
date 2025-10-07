class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # create a dictionary to store the index of each number in array.
        dic = {}
        for i in range(0, len(nums)):
            dic[nums[i]] = i
        
        for i in range(len(nums)):
            dif = target - nums[i]
            if (dif) in dic:
                if dic[dif] == i:
                    continue
                return [i, dic[dif]]

    def twoSum2(self, nums, target):        # a better solution
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:             # if diff is in the list but not yet in the hashmap, we will find it later
                return [prevMap[diff], i]   # but in reverse order when the loop reaches diff, finds the original num.  
            prevMap[n] = i



sol = Solution()
print(sol.twoSum([3,2,4], 6))