import unittest

def optimal_bst(keys, f, n):
    cost = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        cost[i][i] = f[i]
        print(cost)

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')

            f_sum = sum(f[i:j + 1])


            for r in range(i, j + 1):
                left_cost = cost[i][r - 1] if r > i else 0
                right_cost = cost[r + 1][j] if r < j else 0
                total_cost = left_cost + right_cost + f_sum
                cost[i][j] = min(cost[i][j], total_cost)
                print(cost)
                
    return cost[0][n - 1]

class TestOptimalBST(unittest.TestCase):
    
    def test_example1(self):
        keys = [5, 6]
        f = [17, 25]
        n = len(keys)
        min_cost = optimal_bst(keys, f, n)
        self.assertEqual(min_cost, 59)  

    def test_example2(self):
        keys = [10, 12, 20]
        f = [34, 8, 50]
        n = len(keys)
        min_cost = optimal_bst(keys, f, n)
        self.assertEqual(min_cost, 142)  

    def test_example3(self):
        keys = [10, 12]
        f = [10, 20]
        n = len(keys)
        min_cost = optimal_bst(keys, f, n)
        self.assertEqual(min_cost, 40)  

if __name__ == '__main__':
    unittest.main()
