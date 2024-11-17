class Solution:
    def longestCommonSubsequence(self, text1, text2):
        memo = {}

        def lcs_helper(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + lcs_helper(i + 1, j + 1)
            else:
                memo[(i, j)] = max(lcs_helper(i + 1, j), lcs_helper(i, j + 1))

            return memo[(i, j)]

        return lcs_helper(0, 0)

# Example usage
solution = Solution()
print(solution.longestCommonSubsequence("abcde", "ace"))  # Output: 3
print(solution.longestCommonSubsequence("abc", "abc"))    # Output: 3
print(solution.longestCommonSubsequence("abc", "def"))    # Output: 0
