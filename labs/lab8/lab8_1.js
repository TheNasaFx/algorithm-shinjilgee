function coinChange(coins, amount) {
    const dp = Array(amount + 1).fill(Infinity);
    dp[0] = 0;
    for (let i = 1; i <= amount; i++) {
        for (const coin of coins) {
            if (i - coin >= 0) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    return dp[amount] === Infinity ? -1 : dp[amount];
}

// Unit test
const assert = require('assert');

assert.strictEqual(coinChange([1, 2, 5], 11), 3);
assert.strictEqual(coinChange([2], 3), -1);
assert.strictEqual(coinChange([1], 0), 0);
assert.strictEqual(coinChange([1, 2, 5], 100), 20);

console.log("All tests passed!");
