def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while r >= l:
        mid = (r + l) // 2

        if nums[mid] == target:
            return mid
        # left sorted portion
        elif nums[mid] >= nums[l]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # right sorted portion
        else:
            if target > nums[r] or target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
    return -1


nums = [3, 1]
target = 1
print(search(nums, target))
