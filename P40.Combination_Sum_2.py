# step1 : sort candidates list
# step2 : do dfs
# step3 :注意，remove duplidate

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.out = []
        self.dfs(target, candidates, 0, 0, [])
        return self.out

    def dfs(self, target, candidates, index, cur_sum, cur_path):
        if cur_sum == target:
            return self.out.append(cur_path[:])
        if cur_sum > target:
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(target, candidates, i + 1, cur_sum + candidates[i], cur_path + [candidates[i]])



