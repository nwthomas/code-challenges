from odd_even_singleton import DoubleSingleton
import unittest


class TestDoubleSingleton(unittest.TestCase):
    def test_instantiates(self):
        """
        Instantiates the class without failing
        """
        ds = DoubleSingleton()
        self.assertIsInstance(ds, DoubleSingleton)

    def test_instantiates_with_none(self):
        """
        Instantiates with None as the default for evenInstance and oddInstance
        """
        ds = DoubleSingleton()
        self.assertEqual(ds.odd_instance, None)
        self.assertEqual(ds.even_instance, None)

    def test_returns_values_in_alternating_pattern(self):
        """
        Returns odd and even instances of the DoubleSingleton class in an alternating
        pattern
        """
        ds = DoubleSingleton()
        ds.add_value("odd")
        ds.add_value("even")
        self.assertEqual(ds.get_instance(), "odd")
        self.assertEqual(ds.get_instance(), "even")
        self.assertEqual(ds.get_instance(), "odd")
        self.assertEqual(ds.get_instance(), "even")


if __name__ == "__main__":
    unittest.main()
