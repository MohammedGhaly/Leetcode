# class Solution:
#     def change(self, amount: int, coins: list[int]) -> int:
#         if amount == 0:
#             return 1
#         memo = {}

#         def dfs(target, start_index):
#             if target == 0:
#                 return 1

#             if target < 0:
#                 return 0

#             if (target, start_index) in memo:
#                 return memo[(target, start_index)]

#             children_sum = 0
#             for idx in range(start_index, len(coins)):
#                 res = dfs(target-coins[idx], idx)
#                 children_sum += res
#                 # memo[target-coins[idx]] = res

#             memo[(target, start_index)] = children_sum
#             return children_sum

#         ch_sum = dfs(amount, 0)
#         return ch_sum


# class Solution:
#     def change(self, amount: int, coins: list[int]) -> int:
#         if amount == 0:
#             return 1
#         # coins.sort()

#         def dfs(start_index, sum: int = 0):
#             if sum + coins[start_index] == amount:
#                 return 1
#             if sum + coins[start_index] > amount:
#                 return 0
#             children_sum = 0
#             for idx in range(start_index, len(coins)):
#                 children_sum += dfs(idx, sum + coins[start_index])

#             return children_sum

#         ch_sum = 0
#         for i in range(len(coins)):
#             ch_sum += dfs(i, 0)
#         return ch_sum

class Solution(object):
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]


sol = Solution()
amount = 5
coins = [1, 2, 5]


res = sol.change(amount, coins)
print(res)
