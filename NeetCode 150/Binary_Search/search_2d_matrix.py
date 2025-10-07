def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    top = 0
    bottom = len(matrix) - 1
    middle = None
    n = len(matrix[0])

    while (top <= bottom):
        middle = (top + bottom) // 2
        if (target >= matrix[middle][0] and target <= matrix[middle][n-1]):
            break
        elif (target < matrix[middle][0] and target <= matrix[middle][n-1]):
            bottom = middle - 1
        else:
            top = middle + 1
    else:
        return False

    top = 0
    bottom = n-1

    while (top <= bottom):
        middle2 = (top + bottom) // 2
        if (target == matrix[middle][middle2]):
            return True
        elif (target < matrix[middle][middle2]):
            bottom = middle2 - 1
        else:
            top = middle2 + 1

    return False
