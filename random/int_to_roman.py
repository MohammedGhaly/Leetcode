class Solution:
    def intToRoman(self, num: int) -> str:
        a = [
            "I", "V",
            "X",  "L",
            "C",  "D",
            "M"
        ]

        res = ""
        place = len(f'{num}')    # 3999 -> 4

        for c in f'{num}':
            n = int(c)
            if n > 5:
                if n == 9:
                    res += f"{a[place*2-2]}{a[place*2]}"
                    place -= 1
                    continue
                else:
                    res += a[place*2-1]
                    n -= 5

            if n == 5:
                res += a[place*2-1]
            elif n == 4:
                res += f"{a[place*2-2]}{a[place*2-1]}"
            else:
                res += (n) * a[place*2-2]
            place -= 1

        return res


sol = Solution()
print(sol.intToRoman(3749))
