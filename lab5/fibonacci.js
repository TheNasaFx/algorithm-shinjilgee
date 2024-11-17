class Fibonacci {
    constructor() {
        this.cache = {};
    }

    fib(n) {
        if (n === 0) {
            return 0;
        } else if (n === 1) {
            return 1;
        }

        if (this.cache[n]) {
            return this.cache[n];
        }

        // Recursively
        this.cache[n] = this.fib(n - 1) + this.fib(n - 2);
        return this.cache[n];
    }
}

module.exports = Fibonacci;
