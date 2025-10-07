class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        sum = n

        def check_palindrome(l, r):
            count = 0
            while l >= 0 and r < n:
                if not s[l] == s[r]:
                    break
                count += 1
                l -= 1
                r += 1
            return count

        for i in range(len(s)):
            # check odd
            sum += check_palindrome(i-1, i+1)
            # check even
            sum += check_palindrome(i, i+1)

        return sum


sol = Solution()
s = "aaaa"
print(sol.countSubstrings(s))
