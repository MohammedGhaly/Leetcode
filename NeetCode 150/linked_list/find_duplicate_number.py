class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        fast = slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow


sol = Solution()
l = [3, 1, 3, 2, 4]
print(sol.findDuplicate(l))

# for i in range(1, 1):
#     print(i)
