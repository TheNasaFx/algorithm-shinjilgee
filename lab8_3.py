def assignBikes(students, bikes):
    n = len(students)
    m = len(bikes)
    distances = []

    for i in range(n):
        for j in range(m):
            dist = abs(students[i][0] - bikes[j][0]) + abs(students[i][1] - bikes[j][1])
            distances.append((dist, i, j))

    distances.sort()
    result = [-1] * n
    bike_used = [False] * m

    for dist, student, bike in distances:
        if result[student] == -1 and not bike_used[bike]:
            result[student] = bike
            bike_used[bike] = True

    return result

# Unit test
import unittest
class TestAssignBikes(unittest.TestCase):
    def test_assign_bikes(self):
        self.assertEqual(assignBikes([(0, 0), (1, 1)], [(0, 1), (4, 3), (2, 1)]), [0, 2])
        self.assertEqual(assignBikes([(0, 0)], [(0, 1)]), [0])
        self.assertEqual(assignBikes([(0, 0), (2, 2)], [(1, 1), (3, 3)]), [0, 1])

if __name__ == "__main__":
    unittest.main()
