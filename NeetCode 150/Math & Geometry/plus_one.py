class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = (digits[i] + 1) % 10
            if digits[i] > 0:
                return digits
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits