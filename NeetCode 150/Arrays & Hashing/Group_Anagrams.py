def is_anagram(s1, s2) -> True:
    # check length of strings are equal or not
    if len(s1) != len(s2):
        return False
    for char in s1:
        if char not in s2:
            return False
    return True

def get_key(s) -> int:
    res = 1
    for char in s:
        res = res * ord(char)
    for char in s:
        res = res + ord(char)
    return res

class Solution(object):
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash = {}
        
        for i in range(0, len(strs)):
            key = get_key(strs[i])
            if key in hash:
                hash[key].append(strs[i])
            else:
                hash[key] = [strs[i]]
                
        resulting_list = []
        for key in hash:
            resulting_list.append(hash[key])
        print(resulting_list)

sol = Solution()
sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    
    
