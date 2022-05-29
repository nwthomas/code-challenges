from rotate_image import rotate
import unittest

class TestRotate(unittest.TestCase):
    small_2d_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    large_2d_list = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
    ]

    def test_rotates_small_list(self):
        """Rotates a small 2d list in place"""
        rotate(self.small_2d_list)
        self.assertEqual(self.small_2d_list, [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3],
        ])

    def test_rotates_large_list(self):
        """Rotates a large 2d list in place"""
        rotate(self.large_2d_list)
        self.assertEqual(self.large_2d_list, [
            [1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4],
            [5, 5, 5, 5, 5],
        ])

    def test_raises_typeerror_if_martrix_is_not_list(self):
        """Raises a TypeError if argument is not of type list"""
        def result():
            rotate(5)
            
        self.assertRaises(TypeError, result)

    def test_raises_typeerror_if_row_is_not_list(self):
        """Raises a TypeError if one of the rows is not of type list"""
        invalid_2d_list = [[1, 2, 3], 4, [7, 8, 9]]

        def result():
            rotate(invalid_2d_list)

        self.assertRaises(TypeError, result)

if __name__ == "__main__":
    unittest.main()