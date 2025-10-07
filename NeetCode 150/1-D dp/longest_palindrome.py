class Solution:
    def check(self, l, r):
        while l >= 0 and r < len(self.s):
            if self.s[l] == self.s[r]:
                if (r+1-l) > self.res_len:
                    self.res_len = r+1-l
                    self.res = self.s[l: r+1]
                r += 1
                l -= 1
            else:
                break

    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        self.res_len = 0
        self.s = s

        for i in range(len(s)):
            self.check(i, i)
            self.check(i, i+1)

        return self.res


s = "babbadab"
s = "ccb"
sol = Solution()
print(sol.longestPalindrome(s))
