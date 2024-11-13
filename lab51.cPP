#include <iostream>
#include <unordered_map>
#include <cassert>

class Fibonacci {
public:
    Fibonacci() {}

    int fib(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        }

        if (cache.find(n) != cache.end()) {
            return cache[n];
        }

        // Recursively
        cache[n] = fib(n - 1) + fib(n - 2);
        return cache[n];
    }

private:
    std::unordered_map<int, int> cache;
};

void runTests() {
    Fibonacci fibonacci;

    // Base cases
    assert(fibonacci.fib(0) == 0);
    assert(fibonacci.fib(1) == 1);

    // Small numbers
    assert(fibonacci.fib(2) == 1);
    assert(fibonacci.fib(3) == 2);
    assert(fibonacci.fib(4) == 3);
    assert(fibonacci.fib(5) == 5);

    // Larger numbers
    assert(fibonacci.fib(10) == 55);
    assert(fibonacci.fib(20) == 6765);
    assert(fibonacci.fib(30) == 832040);

    std::cout << "All tests passed!" << std::endl;
}

int main() {
    Fibonacci fibonacci;

    int n_values[] = {0, 1, 5, 10, 20, 30};
    for (int n : n_values) {
        int result = fibonacci.fib(n);
        std::cout << "F(" << n << ") = " << result << std::endl;
    }

    // Run the unit tests
    runTests();

    return 0;
}
