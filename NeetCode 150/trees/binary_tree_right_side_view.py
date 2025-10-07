class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if root is None:
            return []

        nodes = [root]
        res = []

        while len(nodes):
            res.append(nodes[-1].val)
            nodes = [child for node in nodes for child in [
                node.left, node.right] if child is not None]

        return res


n5 = TreeNode(5)
n4 = TreeNode(4)
n2 = TreeNode(2, None, n5)
n3 = TreeNode(3, None, n4)
n1 = TreeNode(1, n2, n3)

print(Solution().rightSideView(n1))
