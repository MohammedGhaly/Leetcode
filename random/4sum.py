class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        if len(nums) < 4:
            return []
        used = set()
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            frst = i
            for j in range(i+1, len(nums)-2):
                sec = j
                left, right = sec+1, len(nums)-1
                while left < right:
                    total = nums[frst] + nums[sec]+nums[left]+nums[right]
                    if total == target:
                        if f'{nums[frst]},{nums[sec]},{nums[left]},{nums[right]}' not in used:
                            res.append(
                                [nums[frst], nums[sec], nums[left], nums[right]])
                            used.add(
                                f'{nums[frst]},{nums[sec]},{nums[left]},{nums[right]}')
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    elif total > target:
                        right -= 1
        return res


sol = Solution()
nums = [2, 2, 2, 2, 2]
target = 8
print(sol.fourSum(nums, target))
