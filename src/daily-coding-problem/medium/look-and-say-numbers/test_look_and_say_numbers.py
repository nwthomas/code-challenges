from look_and_say_numbers import find_nth_look_and_say_number
import unittest


class TestFindNthLookAndSayNumber(unittest.TestCase):
    def test_raises_typeerror_if_arg_not_int(self):
        """Raises a new TypeError if the argument is not of type int"""
        def result(): return find_nth_look_and_say_number({ "test": "test" })
        self.assertRaises(TypeError, result)

    def test_gets_small_nth_number(self):
        """Gets the look and say number of an Nth number that is small"""
        result = find_nth_look_and_say_number(5)
        self.assertEqual(result, 111221)
    
    def test_gets_large_nth_number(self):
        """Gets the look and say number of an Nth number that is large"""
        result = find_nth_look_and_say_number(15)
        self.assertEqual(result, 311311222113111231131112132112311321322112111312211312111322212311322113212221)


if __name__ == "__main__":
    unittest.main()