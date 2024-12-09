import unittest

class Solution:
    def longestCommonSubsequence(self, text1, text2):
        memo = {}

        def lcs_helper(i, j):
            # end?
            if i == len(text1) or j == len(text2):
                return 0

            # res memoized?
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + lcs_helper(i + 1, j + 1)
            else:
                memo[(i, j)] = max(lcs_helper(i + 1, j), lcs_helper(i, j + 1))

            return memo[(i, j)]

        return lcs_helper(0, 0)

class TestLongestCommonSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(self.solution.longestCommonSubsequence("abcde", "ace"), 3)  # Example 1
        self.assertEqual(self.solution.longestCommonSubsequence("abc", "abc"), 3)    # Example 2
        self.assertEqual(self.solution.longestCommonSubsequence("abc", "def"), 0)    # Example 3

    def test_empty_strings(self):
        self.assertEqual(self.solution.longestCommonSubsequence("", ""), 0)  # Both strings empty
        self.assertEqual(self.solution.longestCommonSubsequence("abc", ""), 0)  # One string empty
        self.assertEqual(self.solution.longestCommonSubsequence("", "def"), 0)  # Other string empty

    def test_no_common_subsequence(self):
        self.assertEqual(self.solution.longestCommonSubsequence("xyz", "abc"), 0)  

    def test_longer_subsequence(self):
        self.assertEqual(self.solution.longestCommonSubsequence("abcdef", "acf"), 3)  # Subsequence is "acf"

    def test_repeated_characters(self):
        self.assertEqual(self.solution.longestCommonSubsequence("aabbcc", "abc"), 3)  # Subsequence is "abc"

if __name__ == "__main__":
    solution = Solution()
    
    print("Result for 'abcde' and 'ace':", solution.longestCommonSubsequence("abcde", "ace"))  # Output: 3
    print("Result for 'abc' and 'abc':", solution.longestCommonSubsequence("abc", "abc"))    # Output: 3
    print("Result for 'abc' and 'def':", solution.longestCommonSubsequence("abc", "def"))    # Output: 0

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(unittest.defaultTestLoader.loadTestsFromTestCase(TestLongestCommonSubsequence))
    
    print(f"\nRan {result.testsRun} tests.")
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print(f"{len(result.failures)} tests failed.")
