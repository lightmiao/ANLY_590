
## solution 1 :
## combination
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.out = []
        self.dfs(nums, 0, [])
        return self.out

    def dfs(self, nums, index, cur_path):
        self.out.append(cur_path[:])

        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, cur_path + [nums[i]])


## dfs + recursion
# 遍历每一个elem 选与不选它，两种结果，相当于二叉树
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.out = []
        self.dfs(nums, 0, [])
        return self.out

    def dfs(self, nums, index, cur_path):
        if index == len(nums):
            self.out.append(cur_path[:])
            return

        cur_path.append(nums[index])
        self.dfs(nums, index + 1, cur_path)

        cur_path.pop()
        self.dfs(nums, index + 1, cur_path)
