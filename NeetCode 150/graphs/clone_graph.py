# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val: int = 0, neighbors: list = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    created = {}

    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return None
        clone_node = Node(node.val)
        self.created[node.val] = clone_node
        for n in node.neighbors:
            if n.val in self.created:
                clone_node.neighbors.append(self.created[n.val])
            else:
                clone_node.neighbors.append(self.cloneGraph(n))
        return clone_node

    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return None
        clone_node = Node(node.val)
        self.created[node] = clone_node
        for n in node.neighbors:
            if n in self.created:
                clone_node.neighbors.append(self.created[n])
            else:
                clone_node.neighbors.append(self.cloneGraph(n))
        return clone_node


node1 = Node(1)
node2 = Node(2, [node1])

# node3 = Node(3, [node2])
# node4 = Node(4, [node3, node1])

# node3.neighbors.append(node4)
# node2.neighbors.append(node3)

node1.neighbors.append(node2)
# node1.neighbors.append(node4)

node = Solution().cloneGraph(node1)

print(node)
