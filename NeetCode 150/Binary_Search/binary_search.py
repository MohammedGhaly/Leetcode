def search(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        cur_idx = (l + r) // 2
        if nums[cur_idx] == target:
            return cur_idx
        if nums[cur_idx] > target:
            r = cur_idx - 1
        else:
            l = cur_idx + 1
    return -1


print(search([-1, 0, 3, 5, 9, 12], -1))
