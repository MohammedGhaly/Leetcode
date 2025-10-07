class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adj_matrix = []
        visited = set()
        count = 0

        for i in range(n):
            adj_matrix.append([])

        for e in edges:
            adj_matrix[e[0]].append(e[1])
            adj_matrix[e[1]].append(e[0])

        def dfs(node: int) -> bool:
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj_matrix[node]:
                dfs(neighbor)

        for node in range(n):
            if node in visited:
                continue
            count += 1
            dfs(node)

        return count


n = 1
# edges = [[0, 1], [1, 2], [2, 3], [4, 5], [6, 7]]
edges = []
print(Solution().countComponents(n, edges))
