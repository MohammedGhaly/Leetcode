class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        arr = [amount+1] * (amount+1)
        arr[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                r = i - coin
                if r >= 0:
                    arr[i] = min(arr[r]+1, arr[i])
        return arr[-1] if arr[amount] != amount + 1 else -1


class Solution2:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1


sol = Solution()
sol2 = Solution2()
coins = [186, 419, 83, 408]
amount = 6249
print(sol.coinChange(coins, amount))
print(sol2.coinChange(coins, amount))
