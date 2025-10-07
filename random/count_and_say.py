class Solution:
    def get_rle(self, rle: str) -> str:
        newRle = ""
        count = 0
        prev_char = ""
        for i in range(len(rle)):
            if rle[i] == prev_char:
                count += 1
            else:
                if count > 0:
                    newRle += f'{count}{prev_char}'
                prev_char = rle[i]
                count = 1
        newRle += f'{count}{prev_char}'
        return newRle

    def countAndSay(self, n: int) -> str:
        if (n == 1):
            return "1"

        return self.get_rle(self.countAndSay(n-1))


sol = Solution()
# print(sol.get_rle("21"))
print(sol.countAndSay(30))
