class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        for num in nums:
            new = res.copy()
            for item in new:
                res.append(item + [num])
            res.append([num])

        res.append([])
        return res


print(Solution().subsets([1, 2, 3]))
