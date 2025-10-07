def threeSum(nums: list[int]) -> list[list[int]]:       # O(n^2) --> T
    res = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        r = len(nums)-1
        l = i+1
        while (l < r):
            sum = nums[i] + nums[l] + nums[r]
            if (sum) == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                while (nums[l] == nums[l-1] and l < r):
                    l += 1
            elif (sum) > 0:
                r -= 1
            else:
                l += 1
    return res


print(threeSum([-1, 0, 1, 2, -1, -4]))
