from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)  
        inDegree = [0] * numCourses  

        for course, pre in prerequisites:
            graph[pre].append(course)
            inDegree[course] += 1

        queue = deque([i for i in range(numCourses) if inDegree[i] == 0])

        processed_courses = 0

        while queue:
            current = queue.popleft()
            processed_courses += 1

            for neighbor in graph[current]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        return processed_courses == numCourses

# Example usage
solution = Solution()
print(solution.canFinish(2, [[1, 0]]))  # Output: True
print(solution.canFinish(2, [[1, 0], [0, 1]]))  # Output: False
