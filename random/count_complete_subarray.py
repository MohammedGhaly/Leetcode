class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        hashmap = {}
        distinct = len(set(nums))
        n = len(nums)
        res = 0
        l, r = 0, 0

        while l < n:
            while r < n and len(hashmap) < distinct:
                new = nums[r]
                hashmap[new] = hashmap.get(new, 0) + 1
                r += 1

            if len(hashmap) == distinct:
                res += (n - r + 1)

            remove = nums[l]
            hashmap[remove] -= 1
            if hashmap[remove] == 0:
                hashmap.pop(remove)
            l += 1
        return res


# l = [1, 3, 1, 1]
# l = [5, 5, 5, 5]
l = [1, 3, 1, 2, 2]

s = Solution()

print(s.countCompleteSubarrays(l))
