def rob(nums: list[int]) -> int:
    rob1, rob2 = 0, 0

    for num in nums:
        temp = max(rob1 + num, rob2)
        rob1 = rob2
        rob2 = temp

    return max(rob1, rob2)
