function countPrimes(n) {
    if (n < 2) return 0;
    const isPrime = Array(n).fill(true);
    isPrime[0] = isPrime[1] = false;
    for (let i = 2; i * i < n; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j < n; j += i) {
                isPrime[j] = false;
            }
        }
    }
    return isPrime.filter(Boolean).length;
}

// Unit test
const assert = require('assert');
assert.strictEqual(countPrimes(18), 7);
assert.strictEqual(countPrimes(10), 4);
assert.strictEqual(countPrimes(2), 0);
assert.strictEqual(countPrimes(1), 0);

console.log("All tests passed!");
