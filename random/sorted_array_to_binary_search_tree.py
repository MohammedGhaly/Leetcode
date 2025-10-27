# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        
        def dfs(start, end):
            if start > end or start < 0 or end >= len(nums):
                return None
            
            new_root_index = (start + end) // 2
            new_left = dfs(start, new_root_index - 1)
            new_right = dfs(new_root_index + 1, end)
            root = TreeNode(nums[new_root_index], new_left, new_right)
            return root
            
        return dfs(0, len(nums)-1)

sol = Solution()
nums = [-10,-3,0,5,9]
res = sol.sortedArrayToBST(nums)
print(res)
