from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        # Step 1: Build the graph and in-degree array
        graph = defaultdict(list)  # Adjacency list representation
        inDegree = [0] * numCourses  # Array to track prerequisites count

        for course, pre in prerequisites:
            graph[pre].append(course)
            inDegree[course] += 1

        # Step 2: Initialize the queue with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if inDegree[i] == 0])
        course_order = []

        # Step 3: Process the courses
        while queue:
            current = queue.popleft()
            course_order.append(current)

            for neighbor in graph[current]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all courses are processed
        if len(course_order) == numCourses:
            return course_order
        return []  # Return empty array if it's not possible to finish all courses

# Example usage
solution = Solution()
print(solution.findOrder(2, [[1, 0]]))  # Output: [0, 1]
print(solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # Output: [0, 1, 2, 3] or [0, 2, 1, 3]
print(solution.findOrder(1, []))  # Output: [0]
