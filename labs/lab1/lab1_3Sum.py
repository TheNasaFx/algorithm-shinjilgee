def threeSum(nums):
    nums.sort()  
    res = []  
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                left += 1
                
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                right -= 1
                
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return res

# Test cases
nums1 = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums1))  # Expected: [[-1, -1, 2], [-1, 0, 1]]

nums2 = [0, 1, 1]
print(threeSum(nums2))  # Expected: []

nums3 = [0, 0, 0]
print(threeSum(nums3))  # Expected: [[0, 0, 0]]
