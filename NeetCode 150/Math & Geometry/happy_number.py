class Solution:
    def isHappy(self, n: int):
        hashset = set()
        num = n
        while True:
            sum = 0
            while num > 0:
                digit = num%10
                num = num // 10
                sum += digit**2
            if sum == 1:
                return True
            if sum in hashset:
                return False
            hashset.add(sum)
            num = sum

sol = Solution()
print(sol.isHappy(2))