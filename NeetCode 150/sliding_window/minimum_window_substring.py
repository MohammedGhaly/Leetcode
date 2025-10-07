class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # early return
        if len(s) < len(t):
            return ""
        if s == t:
            return s

        # inits
        window_map = {}
        needed_chars = set()
        l = 0
        l_increased = 0
        r = len(t) - 1
        shortest = None

        for c in t:
            window_map[c] = 1 + window_map.get(c, 0)
            needed_chars.add(c)

        for c in s[0:r]:
            if (c in window_map.keys()):
                window_map[c] = window_map.get(c, 0) - 1

        while (r < len(s) and r >= l):
            if s[r] in needed_chars and window_map[s[r]] >= 0 and not l_increased:
                window_map[s[r]] -= 1

            if not all(list(map(lambda x: x <= 0, window_map.values()))):
                if not s[l] in needed_chars:
                    l += 1
                    l_increased = True
                elif window_map[s[l]] <= 0:
                    r += 1
                    l_increased = False
            else:
                if shortest is None or len(shortest) > r - l + 1:
                    shortest = s[l: r+1]
                if s[l] in needed_chars:
                    window_map[s[l]] = window_map[s[l]] + 1
                l += 1
                l_increased = True

        if shortest == None or l > r:
            return ""
        else:
            return shortest


sol = Solution()

res = sol.minWindow("b", "A")
print(res)
