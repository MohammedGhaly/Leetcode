class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()

        def backtrack(remain, start) -> list[list[int]]:
            if remain == 0:
                return [[]]
            if remain < 0:
                return []
            sols = []
            res = []
            for index in range(start, len(candidates)):
                if candidates[index] == candidates[index - 1] and index > start and not index == 0:
                    continue
                sols = backtrack(remain - candidates[index], index + 1)
                for sol in sols:
                    sol.insert(0, candidates[index])
                res += sols
            return res

        return backtrack(target, 0)


print(Solution().combinationSum2([1, 2], 4))
# print(Solution().combinationSum2([2, 5, 2, 1, 2], 5))
