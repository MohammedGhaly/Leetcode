class Solution:
    def wordBreak(self, s: str, wordDict: list[str]):
        n = len(s)
        dp = [False] * (n + 1)
        dp[-1] = True
        
        for i in range(n-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= n and word == s[i:i+len(word)]:
                    dp[i] = dp[i + len(word)]
                    if dp[i]:
                        break
            else:
                dp[i] = False
        
        return dp[0]


sol = Solution()
s = "cars"
wordDict = ["car","ca","rs"]
print(sol.wordBreak(s, wordDict))