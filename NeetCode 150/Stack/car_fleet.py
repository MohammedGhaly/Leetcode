def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    if (len(position) == 1):
        return 1
    stack = [(position[i], speed[i]) for i in range(len(position))]
    stack.sort(key=lambda x: -x[0])
    idx = 1
    while idx < len(stack):
        if (stack[idx][1] > stack[idx - 1][1]):
            meet_position = get_meet_position(
                stack[idx - 1][0], stack[idx][0], stack[idx - 1][1], stack[idx][1])
            if meet_position <= target:
                # stack[idx-1] = (meet_position, stack[idx - 1][1])
                stack.pop(idx)
                continue
        idx += 1

    return (len(stack))


def get_meet_position(p1, p2, s1, s2):
    return ((p2*s1) - (p1*s2)) / (s1 - s2)


print(carFleet(13, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
# print(carFleet(13, [10, 2, 5, 7, 4, 6, 11], [7, 5, 10, 5, 9, 4, 1]))
