import math


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        if len(points) == k:
            return points
        points.sort(key=lambda p: math.sqrt(p[0]**2 + p[1]**2))
        return points[:k]


points = [[1, 3], [-2, 2]]
k = 1
points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(Solution().kClosest(points, k))

# points = [1, 2, 3, 4, 5, 6, 7, 8]
# points.sort(key=lambda x: x % 2)
# print(points)
