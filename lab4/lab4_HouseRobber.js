function rob(nums) {
    function robHelper(start) {
        if (start >= nums.length) return 0;
        if (memo[start] !== undefined) return memo[start];

        const robCurrent = nums[start] + robHelper(start + 2);
        const skipCurrent = robHelper(start + 1);

        memo[start] = Math.max(robCurrent, skipCurrent);
        return memo[start];
    }

    const memo = [];
    return robHelper(0);
}

// Example usage:
console.log(rob([1, 2, 3, 1])); // Output: 4
console.log(rob([2, 7, 9, 3, 1])); // Output: 12
