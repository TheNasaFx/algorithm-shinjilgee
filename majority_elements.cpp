#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int majorityElement(const vector<int>& nums) {
        int candidate = 0;
        int count = 0;

        // Phase 1: Find a candidate majority element
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }

        // Phase 2: Return the candidate (since we assume a majority element always exists)
        return candidate;
    }
};

int main() {
    Solution sol;
    vector<int> nums1 = {3, 2, 3};
    vector<int> nums2 = {2, 2, 1, 1, 1, 2, 2};

    cout << "Majority element in nums1: " << sol.majorityElement(nums1) << endl;  // Output: 3
    cout << "Majority element in nums2: " << sol.majorityElement(nums2) << endl;  // Output: 2

    return 0;
}
