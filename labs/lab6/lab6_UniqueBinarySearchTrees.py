class Solution:
    def numTrees(self, n):
        dp = [0] * (n + 1)
        
        dp[0] = 1  
        dp[1] = 1  
        
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                left_trees = dp[root - 1]  
                right_trees = dp[nodes - root]  
                dp[nodes] += left_trees * right_trees
        return dp[n]

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.numTrees(3))  # Output: 5
    print(solution.numTrees(1))  # Output: 1
