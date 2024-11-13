class Solution:
    def twoSum(self, nums, target):
        complement_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in complement_map:
                return [complement_map[complement], i]
            
            complement_map[num] = i
        
        return []

# Example usage:
solution = Solution()

nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1))  # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(solution.twoSum(nums2, target2))  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
print(solution.twoSum(nums3, target3))  # Output: [0, 1]
