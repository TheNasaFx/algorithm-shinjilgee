class Solution:
    def coinChange(self, coins, amount):
        memo = {}

        def minCoins(remaining):
            if remaining == 0:
                return 0  
            if remaining < 0:
                return float('inf')  

            if remaining in memo:
                return memo[remaining]

            min_count = float('inf')

            for coin in coins:
                count = minCoins(remaining - coin)  
                if count != float('inf'):  
                    min_count = min(min_count, count + 1)  

            memo[remaining] = min_count
            return min_count

        result = minCoins(amount)
        return result if result != float('inf') else -1  

# Example usage:
solution = Solution()
print(solution.coinChange([1, 2, 5], 11))  # Output: 3 (5 + 5 + 1)
print(solution.coinChange([2], 3))         # Output: -1 (not possible)
print(solution.coinChange([1], 0))         # Output: 0 (no coins needed)
