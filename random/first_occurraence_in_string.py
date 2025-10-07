class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # i, j = len(haystack) - 1, len(needle) - 1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


sol = Solution()
haystack = "adbutsad"
needle = "sad"
print(sol.strStr(haystack, needle))
