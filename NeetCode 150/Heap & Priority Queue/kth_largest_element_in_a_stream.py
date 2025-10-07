import collections


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        nums.sort()
        self.h = nums[-k:]

    def add(self, val: int) -> int:
        if val > self.h[0]:
            heapq.heapreplace(self.h, val)
        return self.h[0]


l = [90, 50, 30, 40, 10, 20]
sol = KthLargest(3, l)
print(sol.add(15))
print(sol.add(25))
print(sol.add(125))
