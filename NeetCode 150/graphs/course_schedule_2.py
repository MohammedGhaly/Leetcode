class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_matrix = {}
        order = []
        order_set, visited = set(), set()

        # fill the adj_matrix
        for c in range(numCourses):
            adj_matrix[c] = []
        for req in prerequisites:
            adj_matrix[req[0]].append(req[1])

        def dfs(index):
            if len(adj_matrix[index]) == 0:
                if index not in order_set:
                    order.append(index)
                    order_set.add(index)
                return True
            else:
                if index in visited:
                    return False
                visited.add(index)
                index_courses = adj_matrix[index].copy()
                for course in index_courses:
                    if not dfs(course):
                        return False
                    adj_matrix[index].remove(course)

                order_set.add(index)
                order.append(index)
                return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order


numCourses = 4
# prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [0, 3]]
prerequisites = [[1, 3], [1, 2], [2, 0], [0, 3]]

print(Solution().findOrder(numCourses, prerequisites))

# s = set()
# s.add(1)
# s.add(2)
# s.add(3)


# print(4 in s)
