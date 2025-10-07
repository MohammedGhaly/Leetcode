class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closestSum = float('inf')

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                total = nums[i]+nums[left]+nums[right]
                if total == target:
                    return target

                if abs(total-target) < abs(closestSum-target):
                    closestSum = total

                if total > target:
                    right -= 1
                else:
                    left += 1

        return closestSum


sol = Solution()
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]

target = 1
r = sol.threeSumClosest(nums, target)
print(r)
