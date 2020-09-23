class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.out = []
        self.dfs(n, k, 0, [])
        return self.out

    def dfs(self, n, k, index, cur_path):
        if len(cur_path) == k:
            return self.out.append(cur_path[:])

        for i in range(index, n):
            self.dfs(n, k, i + 1, cur_path + [i + 1])

