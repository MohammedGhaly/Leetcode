import math


def minEatingSpeed(piles: list[int], h: int) -> int:
    if len(piles) == h:
        return max(piles)
    return recursive(piles, 0, (1, 10**9), 0, h, 0)


def recursive(piles: list[int], idx: int,  speed_range: tuple[int, int], actions_num: int, h, rechoose=0) -> int:
    if actions_num > h:
        return 10**9

    if len(piles) == idx:
        if actions_num == h:
            return speed_range[0]
        else:
            return 10**9

    if piles[idx] / (rechoose + 1) < speed_range[0]:
        return recursive(piles, idx + 1, (max(speed_range[0], math.ceil(piles[idx] / (
            rechoose + 1))), speed_range[1]), actions_num + 1, h)  # yes

    if piles[idx] / (rechoose + 1) > speed_range[1]:
        return recursive(piles, idx, (speed_range[0], min(speed_range[1], math.ceil(
            piles[idx] / (rechoose + 1)))), actions_num + 1, h, rechoose + 1)  # no

    ate_all = recursive(piles, idx + 1, (max(speed_range[0], math.ceil(piles[idx] / (
        rechoose + 1))), speed_range[1]), actions_num + 1, h)  # yes

    not_all = recursive(piles, idx, (speed_range[0], min(speed_range[1], math.ceil(
        piles[idx] / (rechoose + 1)))), actions_num + 1, h, rechoose + 1)  # no

    return min(not_all, ate_all)


print(minEatingSpeed([5, 7], 3))
print(minEatingSpeed([5, 7], 4))
print(minEatingSpeed([3, 6, 7, 11], 8))
