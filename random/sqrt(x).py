class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x+1
        while r-l > 1:
            mid = (r+l)//2
            squared = mid*mid
            if squared < x:
                l = mid
            elif squared > x:
                r = mid
            else:
                return mid
        return l


sol = Solution()
print(sol.mySqrt(0))
