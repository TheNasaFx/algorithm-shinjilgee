#include <iostream>
#include <vector>
#include <cstdlib> // For rand() and srand()
#include <ctime>   // For time()

class Solution {
public:
    int majorityElement(std::vector<int>& nums) {
        return quickselect(nums, 0, nums.size() - 1, nums.size() / 2);
    }

private:
    int partition(std::vector<int>& nums, int left, int right, int pivotIndex) {
        int pivot = nums[pivotIndex];
        std::swap(nums[pivotIndex], nums[right]);
        int storeIndex = left;
        
        for (int i = left; i < right; ++i) {
            if (nums[i] < pivot) {
                std::swap(nums[storeIndex], nums[i]);
                storeIndex++;
            }
        }
        std::swap(nums[right], nums[storeIndex]);
        return storeIndex;
    }

    int quickselect(std::vector<int>& nums, int left, int right, int k) {
        if (left == right) {
            return nums[left];
        }
        
        // Randomly select a pivot index
        int pivotIndex = left + rand() % (right - left + 1);
        pivotIndex = partition(nums, left, right, pivotIndex);
        
        if (k == pivotIndex) {
            return nums[k];
        } else if (k < pivotIndex) {
            return quickselect(nums, left, pivotIndex - 1, k);
        } else {
            return quickselect(nums, pivotIndex + 1, right, k);
        }
    }
};

int main() {
    srand(static_cast<unsigned>(time(0))); // Seed for random number generation

    Solution sol;

    std::vector<int> nums1 = {3, 2, 3};
    std::vector<int> nums2 = {2, 2, 1, 1, 1, 2, 2};

    std::cout << "Majority element in nums1: " << sol.majorityElement(nums1) << std::endl; // Output: 3
    std::cout << "Majority element in nums2: " << sol.majorityElement(nums2) << std::endl; // Output: 2

    return 0;
}
