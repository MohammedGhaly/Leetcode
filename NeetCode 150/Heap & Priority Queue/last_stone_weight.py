import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        n_stones = [-num for num in stones]
        heapq.heapify(n_stones)

        while len(n_stones) > 1:
            s1 = heapq.heappop(n_stones)
            s2 = heapq.heappop(n_stones)
            heapq.heappush(n_stones, abs(s1-s2) * -1)

        if len(n_stones):
            return n_stones[0] * -1
        return 0
