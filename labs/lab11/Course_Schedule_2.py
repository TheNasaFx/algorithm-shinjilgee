from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        #bfs
        # Step 1: Create graph and track prerequisites for each course
        course_graph = defaultdict(list)
        in_degree = [0] * numCourses  # Track the number of prerequisites for each course
        
        # Build the graph and update in-degree counts
        for course, prerequisite in prerequisites:
            course_graph[prerequisite].append(course)
            in_degree[course] += 1
        
        # Step 2: Add courses with no prerequisites to the queue
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
        course_order = []  # List to store the final course order
        
        # Step 3: Process courses using BFS
        while queue:
            current_course = queue.popleft()
            course_order.append(current_course)
            
            # Decrease the in-degree of neighboring courses
            for dependent_course in course_graph[current_course]:
                in_degree[dependent_course] -= 1
                if in_degree[dependent_course] == 0:
                    queue.append(dependent_course)
        
        # Step 4: Check if all courses have been processed
        if len(course_order) == numCourses:
            return course_order  # Return valid course order
        return []  # Return an empty list if not all courses can be completed
