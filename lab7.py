import unittest

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def value_per_weight(self):
        return self.value / self.weight

def fractional_knapsack(capacity, items):
    items.sort(key=lambda x: x.value_per_weight(), reverse=True)
    total_value = 0

    for item in items:
        if capacity >= item.weight:
            capacity -= item.weight
            total_value += item.value
        else:
            fraction = capacity / item.weight
            total_value += item.value * fraction
            break

    return total_value

class TestFractionalKnapsack(unittest.TestCase):

    def test_knapsack1(self):
        items = [Item(60, 10), Item(100, 20), Item(120, 30)]
        capacity = 50
        result = fractional_knapsack(capacity, items)
        self.assertEqual(result, 240)

    def test_knapsack2(self):
        items = [Item(20, 10), Item(100, 20), Item(60, 10)]
        capacity = 30
        result = fractional_knapsack(capacity, items)
        self.assertEqual(result, 160)

    def test_knapsack3(self):
        items = [Item(10, 5), Item(40, 20), Item(50, 30)]
        capacity = 0
        result = fractional_knapsack(capacity, items)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()
