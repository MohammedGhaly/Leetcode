class Solution(object):
    def convert(self, s : str, numRows : int):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        if len(s) == 1:
            cycle_size = 1
        else:
            cycle_size = (numRows - 1) * 2
            
        zigzaged = ""
        
        for row in range(0, numRows):
            p = 0
            cycle = 0
            while (True):
                p = cycle * cycle_size + row
                if not p < len(s):
                    break
                zigzaged += s[p]
                if (row == 0) or (row == numRows - 1) :
                    p += (numRows -1) * 2
                else:
                    p += (numRows - 1 - row) * 2
                    if not p < len(s):
                        break
                    zigzaged += s[p]
                cycle += 1
                    
        return zigzaged

#    0   1   2   1   0   1   2   1   0   1   2   1                           -> for 3 rwos -> cycle = 4
#    0   1   2   3   2   1   0   1   2   3   2   1   0                       -> for 4 rows -> cycle = 6
#    0   1   2   3   4   3   2   1   0   1   2   3   4   3   2   1   0       -> for 5 rows -> cycle = 8



#       1   2   3   2   1   2   3   2   1   2   3   2       -> for 3 rwos
#       M   o   h   a   m   e   d   G   h   a   l   y
#
#       M       m       h
#       o   a   e   G   a   y
#       h       d       l


#       1   2   3   4   3   2   1   2   3   4   3   2       -> for 4 rows
#       M   o   h   a   m   e   d   G   h   a   l   y

#       M           d
#       o       e   G       y
#       h   m       h   l
#       a           a
# string = "mohamedGhaly"
string = "AB"
solution = Solution()

zigzaged = solution.convert(string, 1)
print(zigzaged)