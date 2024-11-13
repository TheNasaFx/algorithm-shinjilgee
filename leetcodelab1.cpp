#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> complement_map;
        
        for (int i = 0; i < nums.size(); ++i) {
            int num = nums[i];
            int complement = target - num;
            
            if (complement_map.find(complement) != complement_map.end()) {
                return {complement_map[complement], i};
            }
            
            complement_map[num] = i;
        }
        
        return {};
    }
};
