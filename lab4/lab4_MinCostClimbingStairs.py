class Solution:
    def minCostClimbingStairs(self, cost):
        memo = {}

        def minCost(i):
            if i < 0:
                return 0
            if i == 0 or i == 1:
                return cost[i]
            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(minCost(i - 1), minCost(i - 2))
            return memo[i]

        n = len(cost)
        return min(minCost(n - 1), minCost(n - 2))

# Example usage:
solution = Solution()
cost1 = [10, 15, 20]
print(solution.minCostClimbingStairs(cost1))  # Output: 15

cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(solution.minCostClimbingStairs(cost2))  # Output: 6
