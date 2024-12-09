from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks, n):
        if n == 0:
            return len(tasks)

        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        intervals = 0
        while max_heap:
            temp = []
            for _ in range(n + 1):
                if max_heap:
                    temp.append(heapq.heappop(max_heap))

            for count in temp:
                if count + 1 < 0:
                    heapq.heappush(max_heap, count + 1)

            intervals += n + 1 if max_heap else len(temp)

        return intervals

# Example usage:
solution = Solution()
print(solution.leastInterval(["A", "A", "A", "B", "B", "B"], 2))  # Output: 8
print(solution.leastInterval(["A", "C", "A", "B", "D", "B"], 1))  # Output: 6
print(solution.leastInterval(["A", "A", "A", "B", "B", "B"], 3))  # Output: 10
