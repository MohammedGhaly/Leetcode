class Solution:
    def divide(self, dividend: int, divisor: int):
        if (dividend == -2147483648 and divisor == -1):
            return 2147483647
        is_negative = (dividend < 0) ^ (divisor < 0)
        a, b, res = abs(dividend), abs(divisor), 0
        for i in range(32)[::-1]:
            if b << i > a:
                continue
            res += 1 << i
            a -= b*(1 << i)

        return res if not is_negative else -res


sol = Solution()
print(sol.divide(12, 1))