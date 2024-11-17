import unittest
from knapsack import knapsack

class TestKnapsack(unittest.TestCase):
    def test_knapsack(self):
        weights = [1, 2, 3]
        values = [10, 15, 40]
        max_weight = 6
        n = len(values)
        result = knapsack(max_weight, weights, values, n)
        self.assertEqual(result, 65)  

    def test_knapsack_zero_capacity(self):
        weights = [1, 2, 3]
        values = [10, 15, 40]
        max_weight = 0
        n = len(values)
        result = knapsack(max_weight, weights, values, n)
        self.assertEqual(result, 0)

    def test_knapsack_all_items_too_heavy(self):
        weights = [5, 6, 7]
        values = [10, 20, 30]
        max_weight = 4
        n = len(values)
        result = knapsack(max_weight, weights, values, n)
        self.assertEqual(result, 0)

    def test_knapsack_select_optimal_items(self):
        weights = [1, 2, 4, 2, 5]
        values = [5, 3, 5, 3, 2]
        max_weight = 10
        n = len(values)
        result = knapsack(max_weight, weights, values, n)
        self.assertEqual(result, 16)  

if __name__ == '__main__':
    unittest.main()
