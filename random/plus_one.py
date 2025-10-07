class Solution(object):
    def plusOne(self, digits : list[int]):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = 1
        while (i <= len(digits)):
            digits[-i] = (digits[-i] + 1) % 10
            if digits[-i] != 0:
                return digits
            i += 1
        else:
            digits.insert(0, 1)
            return digits
        
        
    def _plusOne(self, digits : list[int]):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = int("".join(map(str, digits))) + 1
        return list(map(int, str(res)))
        
            
            
            
solution = Solution()
digits = [8, 9, 9, 9]
digits = solution._plusOne(digits)
print(digits)