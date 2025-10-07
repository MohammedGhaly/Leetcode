class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                # find least_greater
                least_greater_index = nums[i:].index(min(
                    [j for j in nums[i:] if j > nums[i-1]])) + i
                # swap it with i-1
                temp = nums[least_greater_index]
                nums[least_greater_index] = nums[i-1]
                nums[i-1] = temp
                # sort the rest of the array from i till the end
                nums[i:] = sorted(nums[i:])
                break
        else:
            nums.reverse()


l = [5, 4, 7, 5, 3, 2]
sol = Solution().nextPermutation(l)
print(l)
