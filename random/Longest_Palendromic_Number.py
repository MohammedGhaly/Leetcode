class Solution(object):
    def longestPalindrome(self, s):
        return s
#           x   y            
    #   1   1   2   3   5   8   13  21  34  55
    def fib(self, n, i, x, y):
        if (n <= 2):        #   for faster execution of 1 and 2
            return 1
        
        if i > n:           #   base condition
            return y
        
        new = x + y
        x = y
        y = new
        
        return self.fib(n, i + 1, x, y)
    
    def fibonacci(self, n : int):
        return self.fib(n, 2, 0, 1)








solution = Solution()
res = solution.fibonacci(25)
print(res)