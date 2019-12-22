from validate_courses import validate_courses
import unittest


class TestValidateCourses(unittest.TestCase):
    def test_courses_short_list(self):
        """
        This test checks to see if a valid short list of courses is returned from the graph
        that is passed into validate_courses() as an argument
        """
        courses = {'CSC300': ['CSC100', 'CSC200'],
                   'CSC200': ['CSC100'], 'CSC100': []}
        result = validate_courses(courses)
        self.assertEqual(result, ['CSC300', 'CSC200', 'CSC100'])

    def test_courses_long_list(self):
        """
        This test checks to see if a valid long list of courses is returned from the graph
        that is passed into validate_courses() as an argument
        """
        courses = {'CSC300': ['CSC100', 'CSC200'],
                   'CSC200': ['CSC100'], 'CSC100': [],
                   'BIO101': [], 'BIO102': ['BIO101'],
                   'BIO300': ['BIO101', 'BIO102'],
                   'BIO404': ['BIO101', 'BIO102', 'BIO300']}
        result = validate_courses(courses)
        self.assertEqual(
            result, ['CSC300', 'CSC200', 'CSC100', 'BIO101', 'BIO102', 'BIO300', 'BIO404'])

    def test_return_empty_invalid_list(self):
        """
        This test checks to see if an empty list is returned if an invalid graph of courses
        is passed into 
        """
        courses = {'CSC300': ['CSC100', 'CSC200'],
                   'CSC200': ['CSC100']}
        result = validate_courses(courses)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
