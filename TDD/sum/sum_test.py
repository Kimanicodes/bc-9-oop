import unittest
from my_sum import addition


class TestsSum(unittest.TestCase):
    def test_sum1(self):
        """Test sum of Numbers passed to be 10 for 4 and 6"""
        self.assertEqual(addition(4, 6), 10)
        """Test the function does not return a None value"""

    def test_sum2(self):
        self.assertIsNotNone(addition(1, 2))

    def test_not_sum(self):
        """Test that the sum of numbers 7 and 8 is only 15"""
        self.assertNotEqual(addition(2, 23456789), 2)

    def test_negative_numbers(self):
        """Test negative numbers"""
        self.assertEqual(addition(-10, -20), -30)

    def test_for_no_arguments(self):
        """Test no arguments passed"""
        self.assertEqual(addition(), None, msg="No arguments passed")

    def test_not_numbers(self):
        """Test to make sure the"""
        result = addition('', '')
        self.assertNotEqual(type(result), int, msg='This is not an integer')


if __name__ == "__main__":
    unittest.main()
