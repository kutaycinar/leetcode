from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]

        for c1, c2 in prerequisites:
            graph[c1].append(c2)

        visited = set()

        def dfs(v):
            if v in visited:
                return False

            visited.add(v)

            for neighbour in graph[v]:
                if not dfs(neighbour):
                    return False

            visited.remove(v)
            graph[v] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


# Time:  O(n)
# Space: O(n)
