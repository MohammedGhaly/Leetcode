class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if len(cost) <= 2:
            return min(cost)

        for i in range(2, len(cost)):
            if cost[i - 1] < cost[i - 2]:
                cost[i] += cost[i-1]
            else:
                cost[i] += cost[i-2]

        return min(cost[-2:])


l = [10, 15, 20]
print(Solution().minCostClimbingStairs(l))
