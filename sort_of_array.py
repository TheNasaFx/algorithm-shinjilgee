class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def quickSort(nums, low, high):
            if low < high:
                p = partition(nums, low, high)
                
                quickSort(nums, low, p - 1)
                quickSort(nums, p + 1, high)

        def partition(nums, low, high):
            pivot = nums[high]
            i = low - 1
            for j in range(low, high):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1], nums[high] = nums[high], nums[i + 1]
            return i + 1

        quickSort(nums, 0, len(nums) - 1)
        return nums

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [5, 2, 3, 1]
    sorted_nums1 = sol.sortArray(nums1)
    print("Sorted nums1: {}".format(sorted_nums1))  # Output: [1, 2, 3, 5]

    # Example 2
    nums2 = [5, 1, 1, 2, 0, 0]
    sorted_nums2 = sol.sortArray(nums2)
    print("Sorted nums2: {}".format(sorted_nums2))  # Output: [0, 0, 1, 1, 2, 5]
