def countPrimes(n):
    if n < 2:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    return sum(is_prime)

import unittest
# Unit test
class TestCountPrimes(unittest.TestCase):
    def test_count_primes(self):
        self.assertEqual(countPrimes(18), 7)
        self.assertEqual(countPrimes(10), 4)
        self.assertEqual(countPrimes(2), 0)
        self.assertEqual(countPrimes(1), 0)

if __name__ == "__main__":
    unittest.main()
