import unittest
from lesson17_1 import get_number_for_index, get_empty_list, get_index_from_numbers


class Test_my(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_number_for_index(3, 2), 15)

    def test_2(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_3(self):
        a = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_4(self):
        a = []
        mas = [
            [1, 1, 1, 1],
            [2, 2, 1, 4],
            [1, 7, 6, 5],
            [2, 3, 2, 1],
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_5(self):
        self.assertEqual(get_index_from_numbers(15), (3, 2))

    def test_6(self):
        self.assertEqual(get_index_from_numbers(7), (1, 2))

    def test_7(self):
        self.assertEqual(get_index_from_numbers(1), (0, 0))


if __name__ == "__main__":
    unittest.main()
