class Solution:
    def climbStairs(self, n):
        memo = {}

        def helper(steps):
            if steps <= 1:
                return 1
            
            if steps in memo:
                return memo[steps]

            # Recursive 
            memo[steps] = helper(steps - 1) + helper(steps - 2)
            return memo[steps]

        # Start the helper function
        return helper(n)

# Example usage
solution = Solution()
print(solution.climbStairs(2))  # Output: 2
print(solution.climbStairs(3))  # Output: 3
