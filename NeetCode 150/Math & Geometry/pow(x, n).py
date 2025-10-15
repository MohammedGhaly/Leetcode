class Solution:
    # iteration -> brute force
    def myPow2(self, x: float, n: int) -> float:
        # X powerof n
        if x == 0 : return 0
        if n == 0 : return 1
        
        is_negative = n < 0
        res = 1
        for i in range(abs(n)):
            res*=x
        
        if is_negative:
            return 1/res
        return res


    # recursive -> recommended
    def myPow(self, x: float, n: int) -> float:
        # X powerof n
        if x == 0 : return 0
        if x == 1 : return x
        is_negative = n < 0
        
        def dfs(nn):
            if nn == 0 : return 1
            if nn == 1 : return x
            
            if nn%2:
                return x * dfs(nn-1)
        
            r = dfs(nn/2)
            return r*r
        
        res = dfs(abs(n))
        
        if is_negative:
            return 1/res
        return res
        
sol = Solution()
print(sol.myPow(2, -2))