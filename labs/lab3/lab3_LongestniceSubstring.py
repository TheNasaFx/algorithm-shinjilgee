class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub: str) -> bool:
            return all(char.lower() in sub and char.upper() in sub for char in sub)

        def partition(s: str) -> str:
            if len(s) < 2:
                return ""

            for i, char in enumerate(s):
                if char.lower() not in s or char.upper() not in s:
                    left = partition(s[:i])
                    right = partition(s[i + 1:])
                    
                    return left if len(left) >= len(right) else right
            
            return s if is_nice(s) else ""

        return partition(s)

# Example usage:
sol = Solution()

# Test case 1
s1 = "YazaAay"
print(sol.longestNiceSubstring(s1))  # Expected output: "aAa"

# Test case 2
s2 = "Bb"
print(sol.longestNiceSubstring(s2))  # Expected output: "Bb"

# Test case 3
s3 = "c"
print(sol.longestNiceSubstring(s3))  # Expected output: ""
