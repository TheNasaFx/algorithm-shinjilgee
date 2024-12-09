import heapq

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        # The min-heap (priority queue)
        min_heap = []
        # Keep track of the visited points
        visited = [False] * n
        # Start from the first point
        visited[0] = True
        total_cost = 0
        edges_used = 0
        
        # Function to calculate the Manhattan distance between two points
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        # Add the edges from point 0 to the heap
        for i in range(1, n):
            cost = manhattan_distance(points[0], points[i])
            heapq.heappush(min_heap, (cost, i))
        
        # Prim's Algorithm to find MST
        while edges_used < n - 1:
            cost, point = heapq.heappop(min_heap)
            
            # If the point is already visited, we skip it
            if visited[point]:
                continue
            
            # Otherwise, we add the cost and mark the point as visited
            visited[point] = True
            total_cost += cost
            edges_used += 1
            
            # Add new edges from the current point to the heap
            for i in range(n):
                if not visited[i]:
                    new_cost = manhattan_distance(points[point], points[i])
                    heapq.heappush(min_heap, (new_cost, i))
        
        return total_cost

# Example usage
solution = Solution()
print(solution.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))  # Output: 20
print(solution.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))  # Output: 18
