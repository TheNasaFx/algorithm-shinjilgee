function majorityElement(nums) {
    function majorityElementRec(nums, left, right) {
        if (left === right) {
            return nums[left];
        }

        const mid = Math.floor((left + right) / 2);
        const leftMajority = majorityElementRec(nums, left, mid);
        const rightMajority = majorityElementRec(nums, mid + 1, right);

        if (leftMajority === rightMajority) {
            return leftMajority;
        }

        const leftCount = countInRange(nums, leftMajority, left, right);
        const rightCount = countInRange(nums, rightMajority, left, right);

        return leftCount > rightCount ? leftMajority : rightMajority;
    }

    function countInRange(nums, num, left, right) {
        let count = 0;
        for (let i = left; i <= right; i++) {
            if (nums[i] === num) {
                count++;
            }
        }
        return count;
    }

    return majorityElementRec(nums, 0, nums.length - 1);
}

// Example usage
const nums1 = [3, 2, 3];
const nums2 = [2, 2, 1, 1, 1, 2, 2];
console.log(majorityElement(nums1));  // Output: 3
console.log(majorityElement(nums2));  // Output: 2
