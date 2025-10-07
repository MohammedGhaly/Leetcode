class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        graph = [[] for i in range(numCourses)]
        visited = set()
        # fill the graph
        for preq in prerequisites:
            graph[preq[0]].append(preq[1])

        def dfs(index, path=[]) -> bool:
            if index in visited:
                return True
            if len(graph[index]) == 0:
                return True
            if index in path:
                return False

            new_path = path.copy()
            new_path.append(index)
            for child in graph[index]:
                if not dfs(child, new_path):
                    return False
            visited.add(index)
            return True

        for index, node in enumerate(graph):
            if dfs(index) == False:
                return False
        return True


c = [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]
print(Solution().canFinish(20, c))
