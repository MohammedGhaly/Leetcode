import math

class Solution:
    def countBits(self, n: int):
        # if n == 0:
        #     return [0]
        # if n ==1 :
        #     return [0, 1]
        
        # res = [0, 1]
        
        # for i in range(2, n+1):
        #     level = math.floor(math.log2(i))
        #     level_start = 1<<(level-1)
        #     level_mid = level_start+ 2**(level-1)+(2**(level-1))/2
            
        #     if i <= level_mid:
        #         res.append(res[i-(2**level)//2])
        #     else:
        #         res.append(res[i-(2**level)]+1)
        
        # return res
        
        if n == 0:
            return [0]

        dp = [0] * (n + 1)
        
        for i in range(1, n+1):
            back = 2 ** math.floor(math.log2(i))
            dp[i] = dp[i-back]+1
        return dp
            
            
        
            

sol = Solution()
print(sol.countBits(8))