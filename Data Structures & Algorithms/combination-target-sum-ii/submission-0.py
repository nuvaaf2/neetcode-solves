class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort() 
        res = []

        def backtrack(start_index, current_sum, path):
            if current_sum == target:
                res.append(path[:])
                return
            if current_sum > target:
                return

            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                
                backtrack(i + 1, current_sum + candidates[i], path)
                
                
                path.pop()

        backtrack(0, 0, [])
        return res