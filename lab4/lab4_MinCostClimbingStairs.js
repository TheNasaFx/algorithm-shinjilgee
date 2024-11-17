function minCostClimbingStairs(cost) {
    const memo = {};
    
    function minCost(i) {
        if (i < 0) return 0;
        if (i === 0 || i === 1) return cost[i];
        if (memo[i] !== undefined) return memo[i];
        
        memo[i] = cost[i] + Math.min(minCost(i - 1), minCost(i - 2));
        return memo[i];
    }
    
    const n = cost.length;
    return Math.min(minCost(n - 1), minCost(n - 2));
}

// Example usage:
const cost1 = [10, 15, 20];
console.log(minCostClimbingStairs(cost1)); // Output: 15

const cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1];
console.log(minCostClimbingStairs(cost2)); // Output: 6
