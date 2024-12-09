from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        # Step 1: Initialize the graph and transitive closure matrix
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]
        
        # Step 2: Perform DFS to fill transitive closure
        def dfs(course, target):
            if isPrerequisite[course][target]:
                return
            isPrerequisite[course][target] = True
            for neighbor in graph[target]:
                dfs(course, neighbor)
        
        for course in range(numCourses):
            for neighbor in graph[course]:
                dfs(course, neighbor)
        
        # Step 3: Answer the queries
        return [isPrerequisite[u][v] for u, v in queries]

# Example usage
solution = Solution()
print(solution.checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]))  # Output: [False, True]
print(solution.checkIfPrerequisite(2, [], [[1, 0], [0, 1]]))        # Output: [False, False]
print(solution.checkIfPrerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]))  # Output: [True, True]
