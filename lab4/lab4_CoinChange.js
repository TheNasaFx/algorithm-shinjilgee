function coinChange(coins, amount) {
    function minCoins(coins, amount, memo) {
        if (amount === 0) return 0;
        if (amount < 0) return Infinity;
        if (memo[amount] !== undefined) return memo[amount];

        let min = Infinity;
        for (let coin of coins) {
            let res = minCoins(coins, amount - coin, memo);
            if (res !== Infinity) {
                min = Math.min(min, res + 1);
            }
        }
        memo[amount] = min;
        return min;
    }

    const result = minCoins(coins, amount, {});
    return result === Infinity ? -1 : result;
}

// Example usage:
console.log(coinChange([1, 2, 5], 11)); // Output: 3
console.log(coinChange([2], 3)); // Output: -1
console.log(coinChange([1], 0)); // Output: 0
