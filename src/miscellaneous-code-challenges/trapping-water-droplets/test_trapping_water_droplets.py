from trapping_water_droplets import trap_water_droplets
import unittest

class TestTrapWaterDroplets(unittest.TestCase):
    matrix1 = [
        ["E", "W", "E", "W", "E", "W"],
        ["E", "W", "E", "W", "E", "W"],
        ["E", "W", "E", "W", "E", "W"],
    ]

    matrix2 = [
        ["E", "E", "E", "W", "E", "W"],
        ["E", "W", "E", "W", "E", "W"],
        ["E", "W", "E", "W", "E", "W"],
    ]

    matrix3 = [
        ["E", "E", "E", "E", "E", "W"],
        ["E", "W", "E", "E", "E", "W"],
        ["E", "W", "E", "E", "E", "W"],
        ["E", "W", "E", "W", "E", "W"],
    ]

    matrix4 = [
        ["W", "E", "E", "E", "E", "W"],
        ["W", "W", "E", "E", "E", "W"],
        ["W", "W", "E", "E", "E", "W"],
        ["W", "W", "E", "W", "E", "W"],
    ]

    matrix5 = [
        ["E", "E", "E"],
        ["E", "E", "E"],
        ["E", "E", "E"],
    ]

    matrix6  = [
        ["W", "W", "W"],
        ["W", "W", "W"],
        ["W", "W", "W"],
    ]

    def test_handles_multiple_tall_walls(self):
        result = trap_water_droplets(self.matrix1)
        self.assertEqual(result, 6)

    def test_handles_spillage_from_short_wall(self):
        result = trap_water_droplets(self.matrix2)
        self.assertEqual(result, 5)
        
    def test_handles_spillage_from_short_wall(self):
        result = trap_water_droplets(self.matrix3)
        self.assertEqual(result, 8)

    def test_handles_two_large_walls_with_small_walls_between(self):
        result = trap_water_droplets(self.matrix4)
        self.assertEqual(result, 12)

    def test_can_handle_completely_empty_matrix(self):
        result = trap_water_droplets(self.matrix5)
        self.assertEqual(result, 0)

    def test_can_handle_matrix_of_all_walls(self):
        result = trap_water_droplets(self.matrix6)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()