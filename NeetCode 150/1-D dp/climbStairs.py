def climbStairs(n: int, memo={}) -> int:
    if n < 3:
        return n
    elif n in memo:
        return memo[n]

    else:
        res = climbStairs(n-1, memo) + climbStairs(n-2, memo)
        memo[n] = res
        return res


print(climbStairs(5))
