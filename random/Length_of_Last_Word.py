class Solution(object):
    def lengthOfLastWord(self, s : str):
        """
        :type s: str
        :rtype: int
        """
        i = -1
        list = s.split(' ')
        while (True):
            if len(list[i]) != 0 :
                return len(list[i])
            i = i - 1
            
            
solution = Solution()
string = "Hello World "
res = solution.lengthOfLastWord(string)
print(f'res = {res}')

