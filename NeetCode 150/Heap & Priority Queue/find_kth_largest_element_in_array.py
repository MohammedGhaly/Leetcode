import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # O(k log(n))
        heap = [-n for n in nums]
        heapq.heapify(heap)
        for i in range(k-1):
            heapq.heappop(heap)
        return heap[0] * -1


nums = [3, 2, 1, 5, 6, 4]
k = 2

print(Solution().findKthLargest(nums, k))
