import unittest

class Fibonacci:
    def __init__(self):
        self.cache = {}

    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        if n in self.cache:
            return self.cache[n]
        
        # Recursively 
        self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.cache[n]

class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_base_cases(self):
        self.assertEqual(self.fibonacci.fib(0), 0)  # F(0) = 0
        self.assertEqual(self.fibonacci.fib(1), 1)  # F(1) = 1

    def test_small_numbers(self):
        self.assertEqual(self.fibonacci.fib(2), 1)  # F(2) = 1
        self.assertEqual(self.fibonacci.fib(3), 2)  # F(3) = 2
        self.assertEqual(self.fibonacci.fib(4), 3)  # F(4) = 3
        self.assertEqual(self.fibonacci.fib(5), 5)  # F(5) = 5

    def test_larger_numbers(self):
        self.assertEqual(self.fibonacci.fib(10), 55)  # F(10) = 55
        self.assertEqual(self.fibonacci.fib(20), 6765)  # F(20) = 6765
        self.assertEqual(self.fibonacci.fib(30), 832040)  # F(30) = 832040

if __name__ == "__main__":
    fibonacci = Fibonacci()
    
    n_values = [0, 1, 5, 10, 20, 30]
    for n in n_values:
        result = fibonacci.fib(n)
        print(f"F({n}) = {result}")

    # Run the unit tests
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
