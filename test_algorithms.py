import unittest
from algorithms import file_hevleh, merge_sort, insertion_sort, binary_search, find_max

class TestAlgorithms(unittest.TestCase):

    def setUp(self):
        self.raw_data, self.sorted_data = file_hevleh()

    def test_file_hevleh(self):
        self.assertEqual(self.raw_data, [3, 5, 7, 9, 2, 4, 6, 8, 1, 0])
        self.assertEqual(self.sorted_data, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_merge_sort(self):
        sorted_nums = merge_sort(self.raw_data)
        self.assertEqual(sorted_nums, self.sorted_data)

    def test_insertion_sort(self):
        sorted_nums = insertion_sort(self.raw_data.copy())
        self.assertEqual(sorted_nums, self.sorted_data)

    def test_binary_search_found(self):
        target = 7
        sorted_data = merge_sort(self.raw_data)
        index = binary_search(sorted_data, 0, len(sorted_data) - 1, target)
        self.assertEqual(index, sorted_data.index(target))

    def test_binary_search_not_found(self):
        target = 10
        sorted_data = merge_sort(self.raw_data)
        index = binary_search(sorted_data, 0, len(sorted_data) - 1, target)
        self.assertEqual(index, -1)

    def test_find_max(self):
        max_num = find_max(self.raw_data, 0, len(self.raw_data) - 1)
        self.assertEqual(max_num, max(self.raw_data))

if __name__ == "__main__":
    unittest.main()
