class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n < 0:
        #     return False
        # cur = n
        # while True:
        #     if cur == 1:
        #         return True
        #     cur = cur/4
        #     if cur < 1:
        #         return False

        # another solution
        if n < 1:
            return False
        b = bin(n)
        print(b)
        print(b.index("1"))
        return b.count("1") == 1 and len(b) % 2 == 1


sol = Solution()
print(sol.isPowerOfFour(-1))
