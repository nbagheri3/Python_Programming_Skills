# ----------------------------------------------------------------------
# Name:      unittest
# Purpose:   Create a unit test for two functions in a unittest module
# Author(s): Dasom Lee and Nahal Bagheri
# Date:      03/23/2023
# ----------------------------------------------------------------------
import unittest
import homework6 as hw6


class TestFinalGrade(unittest.TestCase):
    """

    Test case for the normal execution of the final_grade method
    """

    def setUp(self):
        """
        setUp method is invoked prior to each test.

        Create grades for testing
        :return:None
        """
        self.grades = {'Anna': 80, 'Sara': 90, 'John': 70}

    def test_default_argument(self):
        """
        testing the default argument undesired effects

        :return:None
        """
        result = hw6.final_grade(self.grades)
        self.assertEqual(result, {'Anna': 81, 'Sara': 91, 'John': 71})
        self.assertEqual(self.grades, {'Anna': 80, 'Sara': 90,
                                       'John': 70})

    def test_empty_dictionary(self):
        """
        Testing the empty dictionary

        :return:None
        """
        result = hw6.final_grade({})
        self.assertEqual(result, {})

    def test_non_empty_dictionary(self):
        """
        Testing non-empty dictionary undesired effects

        :return:None
        """
        result = hw6.final_grade(self.grades, extra_credit=2)
        self.assertEqual(result, {'Anna': 82, 'Sara': 92, 'John': 72})
        self.assertEqual(self.grades, {'Anna': 80, 'Sara': 90, 'John':
            70})


class TestMostWords(unittest.TestCase):
    """
    Test case for the normal execution of the most_words method
    """

    def test_no_arguments(self):
        """
        Testing of calling the function with no arguments

        :return:None
        """
        result = hw6.most_words()
        self.assertIsNone(result)

    def test_one_argument(self):
        """
        Testing of calling the function with one argument

        :return:None
        """
        result = hw6.most_words('hello')
        self.assertEqual(result, 'hello')

    def test_many_arguments(self):
        """
        Testing of calling the function with many arguments

        :return:None
        """
        result = hw6.most_words('hello', 'Guys', 'this is a test')
        self.assertEqual(result, 'this is a test')