# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []

        res = []
        nodes = [root]

        while len(nodes) > 0:
            res.append([node.val for node in nodes])
            nodes = [child for node in nodes for child in (node.left, node.right) if
                     child is not None]

        return res


n15 = TreeNode(15)
n7 = TreeNode(7)
n20 = TreeNode(20, n15, n7)
n9 = TreeNode(9)
n3 = TreeNode(3, n9, n20)

print(Solution().levelOrder(n3))
