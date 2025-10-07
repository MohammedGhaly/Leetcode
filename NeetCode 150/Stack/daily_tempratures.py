def dailyTemperatures(temperatures: list[int]) -> list[int]:
    res = [0] * len(temperatures)
    temperatures.reverse()
    for idx, current_temp in enumerate(temperatures):
        if idx == 0:
            continue

        check_idx = idx - 1
        if temperatures[check_idx] > current_temp:
            res[idx] = 1
        elif temperatures[check_idx] <= current_temp:
            if res[check_idx] == 0:
                res[idx] = 0
            else:
                check_idx -= res[check_idx]
                while check_idx >= 0:
                    if res[check_idx] == 0:
                        if check_idx == 0:
                            res[idx] = 0
                        else:
                            if temperatures[check_idx] > current_temp:
                                res[idx] = idx - check_idx
                            else:
                                res[idx] = 0
                            break
                    if temperatures[check_idx] > current_temp:
                        res[idx] = idx - check_idx
                        break
                    if temperatures[check_idx] <= current_temp:
                        check_idx -= res[check_idx]

    return list(reversed(res))


print(dailyTemperatures([34, 80, 80, 34, 34, 80, 80, 80, 80, 34]))
# print(dailyTemperatures([55, 38, 53, 81, 61, 93, 97, 32, 43, 78]))
# print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

# print(dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
# print(dailyTemperatures([30, 40, 50, 60]))
# print(dailyTemperatures([30, 60, 90]))
# Input:        temperatures = [73,74,75,71,69,72,76,73]
# Output:                      [1 ,1 ,4 ,2 ,1 ,1 ,0 ,0]
