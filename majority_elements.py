import random

class Solution:
    def majorityElement(self, nums):
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left
            
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            
            nums[right], nums[store_index] = nums[store_index], nums[right]
            
            return store_index
        
        def quickselect(left, right, k):
            if left == right:
                return nums[left]
            
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            
            if k == pivot_index:
                return nums[k]
            elif k < pivot_index:
                return quickselect(left, pivot_index - 1, k)
            else:
                return quickselect(pivot_index + 1, right, k)
        
        # The index of the majority element
        n = len(nums)
        # We need to find the element that appears at index n // 2
        majority_index = n // 2
        
        # Find the element at the majority index
        return quickselect(0, n - 1, majority_index)

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    nums1 = [3, 2, 3]
    nums2 = [2, 2, 1, 1, 1, 2, 2]

    print(sol.majorityElement(nums1))  # Output: 3
    print(sol.majorityElement(nums2))  # Output: 2
