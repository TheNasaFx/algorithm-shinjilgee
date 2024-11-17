def majority_element_rec(nums, left, right):
    if left == right:
        return nums[left]

    mid = (left + right) // 2
    left_majority = majority_element_rec(nums, left, mid)
    right_majority = majority_element_rec(nums, mid + 1, right)

    if left_majority == right_majority:
        return left_majority

    left_count = sum(1 for i in range(left, right + 1) if nums[i] == left_majority)
    right_count = sum(1 for i in range(left, right + 1) if nums[i] == right_majority)

    return left_majority if left_count > right_count else right_majority

def find_majority_element(nums):
    return majority_element_rec(nums, 0, len(nums) - 1)

# Example usage
nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(nums1))  # Output: 3
print(find_majority_element(nums2))  # Output: 2
