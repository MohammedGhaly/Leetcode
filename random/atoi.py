class Solution:
    def myAtoi(self, s: str) -> int:
        stack = []
        positive = True
        i = 0
        leading_zeros = True

        # removing leading whitespaces
        while i < len(s) and s[i] == " ":
            i += 1

        if i >= len(s):
            return 0

        if not s[i].isdigit():
            # if the string starts with a sign
            if s[i] in "+-":
                if s[i] == '-':
                    positive = False
                i += 1
            else:
                return 0

        # number region
        for i, c in enumerate(s[i:]):
            if c.isdigit():
                if c == '0' and leading_zeros:
                    continue
                else:
                    leading_zeros = False
                stack.append(c)
            else:
                break

        # calc int
        sum = 0
        position = 1
        while len(stack):
            digit = int(stack.pop()) * position
            sum += digit
            position *= 10

        if not positive:
            sum = sum * (-1)

        if sum > 2**31 - 1:
            return 2**31
        if sum < 2**31 * -1:
            return 2**31 * -1
        return sum


sol = Solution()
inp = ""
print(sol.myAtoi(inp))
