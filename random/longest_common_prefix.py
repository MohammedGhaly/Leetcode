class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs [0]
        active = ""
        
        for index in range(0, min(len(strs[0]) , len(strs[1]))):
                if (strs[0][index]) == (strs[1][index]):
                    active += (strs[1][index])
                else:
                    break
                if active == "":
                    return ""
        
        for j in range(2, len(strs)): #iterates over the rest of the items
            if not len(active) <= len(strs[j]):
                active = active[:len(strs[j])]
            for index in range(0, len(active)):     # iterates over the chars
                if not (active[index]) == (strs[j][index]):
                    active = active[:(index)]
                    break
                
        return active
    
    
solution = Solution()
a = solution.longestCommonPrefix([""])
print(a)