class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(numbers) -> list[list[int]]:
            if len(numbers) == 0:
                return [[]]

            result = []
            for number in numbers:
                remaining_nums = numbers[:]
                remaining_nums.remove(number)
                sols = backtrack(remaining_nums)
                for sol in sols:
                    sol = sol + [number]
                    result.append(sol)
            return result

        return backtrack(nums)


print(Solution().permute([0]))
