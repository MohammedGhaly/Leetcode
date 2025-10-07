class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        hashmap = {}

        def backtrack(index, path: list[int]):

            if index == len(nums):
                path.sort()
                h = ""
                for value in path:
                    h += str(value)
                if not h in hashmap:
                    hashmap[h] = True
                    res.append(path)
                return

            path1 = path.copy()
            path1.append(nums[index])
            backtrack(index + 1, path1)

            backtrack(index + 1, path.copy())

        backtrack(0, [])
        backtrack(1, [])
        return res


# print(Solution().subsetsWithDup([1, 2, 3]))
print(Solution().subsetsWithDup([4, 4, 4, 1, 4]))
