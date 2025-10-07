class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        hashmap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if (len(digits) == 0):
            return []
        combs = []

        def backtrack(cur='', i=0):
            if len(cur) == len(digits):
                combs.append(cur)
                return
            for letter in hashmap[digits[i]]:
                cur += letter
                backtrack(cur, i+1)
                cur = cur[:-1]

        backtrack()
        return combs


print(Solution().letterCombinations(''))
