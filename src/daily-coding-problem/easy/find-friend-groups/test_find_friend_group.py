from find_friend_groups import find_friend_groups
import unittest

class TestFindFriendGroups(unittest.TestCase):
    def test_returns_two_groups(self):
        """Takes in an adjacency list of friends and returns 2"""
        adj_list = {0: [1, 2], 1: [2], 2: [0], 3: []}
        result = find_friend_groups(adj_list)
        self.assertEqual(result, 2)

    def test_returns_three_groups(self):
        """Takes in an adjacency list of friends and returns 3"""
        adj_list = {0: [1, 2], 1: [0, 5], 2: [0], 3: [6], 4: [], 5: [1], 6: [3]}
        result = find_friend_groups(adj_list)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()