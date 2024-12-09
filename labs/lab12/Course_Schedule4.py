from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]
        
        def dfs(course, target):
            if isPrerequisite[course][target]:
                return
            isPrerequisite[course][target] = True
            for neighbor in graph[target]:
                dfs(course, neighbor)
        
        for course in range(numCourses):
            for neighbor in graph[course]:
                dfs(course, neighbor)
        
        return [isPrerequisite[u][v] for u, v in queries]

# Example usage
solution = Solution()
print(solution.checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]))  # Output: [False, True]
print(solution.checkIfPrerequisite(2, [], [[1, 0], [0, 1]]))        # Output: [False, False]
print(solution.checkIfPrerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]))  # Output: [True, True]
