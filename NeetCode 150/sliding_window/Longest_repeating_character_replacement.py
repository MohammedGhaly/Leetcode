class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = m = 0
        res = 1

        hash_map = {}
        while (r <= len(s) - 1):
            hash_map[s[r]] = hash_map.get(s[r], 0) + 1
            m = max(m, hash_map[s[r]])
            while (not (r - l + 1 - m <= k)):
                hash_map[s[l]] = hash_map.get(s[l]) - 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res


sol = Solution()
res = sol.characterReplacement("ABAB", 2)
print(res)
