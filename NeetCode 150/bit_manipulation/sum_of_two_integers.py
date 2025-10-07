class Solution:
    def getSum(self, a: int, b: int):
        c = 0
        res = 0
        mask = 0xFFFFFFFF

        for p in range(32):
            a_bit = a&(1<<p)
            b_bit = b&(1<<p)
            c_bit = c&(1<<p)
            
            r = c_bit ^ (a_bit ^ b_bit)
            c = ((~c_bit&(1<<p)) & a_bit & b_bit) | (c_bit & (a_bit^b_bit) | (a_bit & b_bit)) 
            c = c<<1
            res = res | r
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        return res

class Solution2:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            cur_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) >= 2
            if cur_bit:
                res |= (1 << i)

        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res
    
sol = Solution()        
res = sol.getSum(-5,-3)
print(res)
