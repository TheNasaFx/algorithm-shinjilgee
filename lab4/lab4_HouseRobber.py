class Solution:
    def rob(self, nums):
        memo = {}

        def robHelper(start):
            if start >= len(nums):
                return 0
            if start in memo:
                return memo[start]

            robCurrent = nums[start] + robHelper(start + 2)
            skipCurrent = robHelper(start + 1)

            memo[start] = max(robCurrent, skipCurrent)
            return memo[start]

        return robHelper(0)

# Example usage:
solution = Solution()
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([2, 7, 9, 3, 1]))  # Output: 12
