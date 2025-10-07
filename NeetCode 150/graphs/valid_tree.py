class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if not n-1 == len(edges):
            return False

        adj_matrix = {}
        visited = set()
        # fill the adj_matrix
        for c in range(n):
            adj_matrix[c] = []
        for e in edges:
            adj_matrix[e[0]].append(e[1])
            adj_matrix[e[1]].append(e[0])

        def dfs(node=0, parent=None):
            if node in visited:
                return False
            visited.add(node)
            for child in adj_matrix[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    return False
            return True

        return dfs() and len(visited) == n


n = 6
edges = [[0, 1], [0, 2], [5, 4], [0, 3]]

print(Solution().validTree(n, edges))
