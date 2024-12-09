from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Step 1: Build the graph and in-degree array
        graph = defaultdict(list)  # Adjacency list representation
        inDegree = [0] * numCourses  # Array to track the number of prerequisites

        for course, pre in prerequisites:
            graph[pre].append(course)
            inDegree[course] += 1

        # Step 2: Initialize the queue with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if inDegree[i] == 0])

        # Step 3: Process courses
        processed_courses = 0

        while queue:
            current = queue.popleft()
            processed_courses += 1

            # Reduce in-degree of neighbors and add to queue if in-degree becomes 0
            for neighbor in graph[current]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all courses have been processed
        return processed_courses == numCourses

# Example usage
solution = Solution()
print(solution.canFinish(2, [[1, 0]]))  # Output: True
print(solution.canFinish(2, [[1, 0], [0, 1]]))  # Output: False
