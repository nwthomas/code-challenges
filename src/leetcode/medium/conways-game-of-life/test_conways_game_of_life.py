from conways_game_of_live import game_of_life
import unittest

class TestGameOfLife(unittest.TestCase):
    def test_does_not_update_all_zeros_board(self):
        """Does nothing to a game board of all 0s"""
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        game_of_life(matrix)
        self.assertEqual(matrix,  [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

    def test_makes_zero_close_to_three_ones_alive(self):
        """Resurrects cell close to three 1s"""
        matrix = [
            [1, 0, 1],
            [0, 0, 0],
            [0, 1, 0]
        ]
        game_of_life(matrix)
        self.assertEqual(matrix, [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ])

    def test_kills_live_cell_next_to_zeroes(self):
        """Kills a 1 cell if it's next to all zeroes"""
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 1, 0]
        ]
        game_of_life(matrix)
        self.assertEqual(matrix, [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

    def test_keeps_cell_with_enough_ones_close_alive(self):
        """Keeps a cell alive if it has 2-3 cells around it that are alive"""
        matrix = [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 0]
        ]
        game_of_life(matrix)
        self.assertEqual(matrix, [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 0]
        ])

    def test_kills_cell_if_more_than_three_live_neighbors(self):
        """Kills a cell if it has more than 5 live neighbors"""
        matrix =  [
            [1, 1, 0],
            [1, 1, 1],
            [0, 0, 0]
        ]
        game_of_life(matrix)
        self.assertEqual(matrix,  [
            [1, 0, 1],
            [1, 0, 1],
            [0, 1, 0]
        ])

    def test_modifies_the_same_matrix_in_place(self):
        matrix = [
            [1, 1, 0],
            [1, 1, 1],
            [0, 0, 0]
        ]
        starting_matrix_memory_address = hex(id(matrix))
        game_of_life(matrix)
        ending_matrix_memory_address = hex(id(matrix))
        self.assertEqual(starting_matrix_memory_address, ending_matrix_memory_address)

if __name__ == "__main__":
    unittest.main()