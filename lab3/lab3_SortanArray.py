class Solution:
    def quick_sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

# Example usage
sol = Solution()
nums1 = [5, 2, 3, 1]
nums2 = [5, 1, 1, 2, 0, 0]
sol.quick_sort(nums1, 0, len(nums1) - 1)
sol.quick_sort(nums2, 0, len(nums2) - 1)
print(nums1)  # Expected output: [1, 2, 3, 5]
print(nums2)  # Expected output: [0, 0, 1, 1, 2, 5]
