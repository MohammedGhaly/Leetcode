class Solution:
    def reverse(self, x: int):
        res = 0
        leading_zeros = True
        pos = 1
        is_negative = x < 0
        x = abs(x)
        
        for i in range(9, -1, -1):
            div = 10**i
            digit = (x // div) % 10
            if digit | (not leading_zeros):
                leading_zeros = False
                res += pos * digit
                pos *= 10
            elif (digit == 0 and leading_zeros):
                continue
        
        if res > 2**31 or res < -2 ** 31:
            return 0
        
        if is_negative: return -res
        return res
                
    

# print(2147483648 // 1000000000)
sol = Solution()
m = sol.reverse(123)
print(m)