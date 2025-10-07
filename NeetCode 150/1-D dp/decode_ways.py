class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1

        def isValid(num: str):
            if num[0] == '0':
                return False
            elif len(num) == 2:
                if num > '26':
                    return False
            return True

        # access the string with i-1
        for i in range(1, len(s)+1):
            if isValid(s[i-1]):
                dp[i] += dp[i-1]
            if i > 1 and isValid(s[i-2:i]):
                dp[i] += dp[i-2]

        return dp[-1]


def isValid(num: str):
    if num[0] == '0':
        return False
    elif len(num) == 2:
        if num > '26':
            return False
    return True


sol = Solution()
res = sol.numDecodings('11106')
print(res)
