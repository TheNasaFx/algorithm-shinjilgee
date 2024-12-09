from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        #bfs
        course_graph = defaultdict(list)
        in_degree = [0] * numCourses  
        
        for course, prerequisite in prerequisites:
            course_graph[prerequisite].append(course)
            in_degree[course] += 1
        
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
        course_order = []  
        
        while queue:
            current_course = queue.popleft()
            course_order.append(current_course)
            
            for dependent_course in course_graph[current_course]:
                in_degree[dependent_course] -= 1
                if in_degree[dependent_course] == 0:
                    queue.append(dependent_course)
        
        if len(course_order) == numCourses:
            return course_order  
        return []  
