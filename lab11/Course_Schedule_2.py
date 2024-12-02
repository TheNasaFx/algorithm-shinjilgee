from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        
        while queue:
            course = queue.popleft()
            order.append(course)
            
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) == numCourses:
            return order
        return []  

solution = Solution()
print(solution.findOrder(2, [[1, 0]]))  # Output: [0, 1]
print(solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # Output: [0, 1, 2, 3] or [0, 2, 1, 3]
print(solution.findOrder(1, []))  # Output: [0]
