import unittest
from rock_paper_scissors import rock_paper_scissors


class Test(unittest.TestCase):
    def test_rock_paper_scissors(self):
        self.assertEqual(rock_paper_scissors(2), [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], [
                         'paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']])
        self.assertEqual(rock_paper_scissors(
            1), [["rock"], ["paper"], ["scissors"]])
        self.assertEqual(rock_paper_scissors(0), [[]])


if __name__ == "__main__":
    unittest.main()
