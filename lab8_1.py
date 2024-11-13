def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


import unittest

class TestCoinChange(unittest.TestCase):
    def test_coin_change(self):
        self.assertEqual(coinChange([1, 2, 5], 11), 3)
        self.assertEqual(coinChange([2, 1], 3), 2)
        self.assertEqual(coinChange([1], 0), 0)
        self.assertEqual(coinChange([1, 2, 5], 100), 20)

if __name__ == "__main__":
    unittest.main()
