def maxProfit(prices: list[int]) -> int:
    max_profit = 0
    l = 0
    r = 1

    while r < len(prices):
        profit = prices[r] - prices[l]
        if profit > 0:
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1
    return max_profit
