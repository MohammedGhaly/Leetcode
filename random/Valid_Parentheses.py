class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_parentheses  = '([{'
        close_parentheses = ')]}'
        stack = []
        
        for ch in s:
            if ch in open_parentheses :
                stack.append(ch)
                continue
            else:
                if len(stack) != 0 and stack[-1] == open_parentheses[close_parentheses.index(ch)]:
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0
                
        
                
                
            
            
            
            
solution = Solution()
str = "[][][[]]"
print(solution.isValid(str))

