class Solution:
    def reverseBits(self, n: int):
        res = 0
        for pos in range(32):
            a = n & (1<<pos)
            a=a>>pos
            res += a<<(31-pos)
        return res


sol = Solution()
r = sol.reverseBits(43261596)

print(r)
        