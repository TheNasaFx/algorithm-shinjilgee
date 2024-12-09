function climbStairs(n) {
    const memo = {};

    function helper(steps) {
        if (steps <= 1) return 1;
        if (memo[steps]) return memo[steps];

        memo[steps] = helper(steps - 1) + helper(steps - 2);
        return memo[steps];
    }

    return helper(n);
}

// Example usage
console.log(climbStairs(2));  // Output: 2
console.log(climbStairs(3));  // Output: 3
