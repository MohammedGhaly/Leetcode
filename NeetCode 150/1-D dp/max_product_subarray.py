class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        cur_max, cur_min = 1, 1

        for n in nums:
            cur_max_times_n_tmp = n*cur_max
            cur_max = max(n*cur_max, n*cur_min, n)
            cur_min = max(cur_max_times_n_tmp, n*cur_min, n)
            res = max(res, cur_max)

        return res
