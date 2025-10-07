def findMin(nums: list[int]) -> int:
    l, r = 0,  len(nums) - 1
    while l < r:
        test = (l + r) // 2
        if (nums[r] > nums[test]):
            r = test
        else:
            l = test + 1

    return nums[l]


nums = [11, 13, 15, 17]
print(findMin(nums))
