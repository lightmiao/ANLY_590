class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.out = []
        self.dfs(target, candidates, 0, 0, [])
        return self.out

    def dfs(self, target, candidates, index, cur_sum, cur_path):
        if cur_sum > target:
            return
        elif cur_sum == target:
            self.out.append(list(cur_path))

        else:
            for i in range(index, len(candidates)):
                self.dfs(target, candidates, i, cur_sum + candidates[i], cur_path + [candidates[i]])
