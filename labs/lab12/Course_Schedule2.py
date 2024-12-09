from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)  
        inDegree = [0] * numCourses  

        for course, pre in prerequisites:
            graph[pre].append(course)
            inDegree[course] += 1

        queue = deque([i for i in range(numCourses) if inDegree[i] == 0])
        course_order = []

        while queue:
            current = queue.popleft()
            course_order.append(current)

            for neighbor in graph[current]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(course_order) == numCourses:
            return course_order
        return []  

# Example usage
solution = Solution()
print(solution.findOrder(2, [[1, 0]]))  # Output: [0, 1]
print(solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # Output: [0, 1, 2, 3] or [0, 2, 1, 3]
print(solution.findOrder(1, []))  # Output: [0]
