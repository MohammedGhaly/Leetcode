class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


# print(bin(2))
# print(bin(-1))
sol = Solution()
r = sol.singleNumber([-1, 2, 2])

print(r)

# print(len(max)-2)
