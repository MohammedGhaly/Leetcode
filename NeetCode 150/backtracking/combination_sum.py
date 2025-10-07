class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        def backtrack(remain, start):
            if remain == 0:
                return [[]]
            if remain < 0:
                return []

            sols = []

            for index in range(start, len(candidates)):
                sol = backtrack(remain - candidates[index], index)
                if sol is not None:
                    for s in sol:
                        s.append(candidates[index])
                    sols += sol
            return sols

        return backtrack(target, 0)


target = 7
candidates = [2, 3, 6, 7]
print(Solution().combinationSum(candidates, target))
