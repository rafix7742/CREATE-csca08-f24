import unittest
from solution_basic_functions import greatest_common_denominator, make_words_to_count, palindrome_names


class TestBasicFunctions(unittest.TestCase):

    def test_greatest_common_denominator(self):
        test_cases = [
            (8, 12, 4),  # Common denominator exists
            (9, 3, 3),   # One number is a multiple of the other
            (7, 13, 1),  # No common denominators other than 1
        ]

        for num1, num2, expected in test_cases:
            with self.subTest(num1=num1, num2=num2):
                result = greatest_common_denominator(num1, num2)
                self.assertEqual(result, expected,
                                 f"Greatest common denominator of {num1} and {num2} is incorrect. Expected: {expected}, Got: {result}")

    def test_palindrome_names(self):
        test_cases = [
            (['Anna', 'Bob', 'Civic', 'David'], ['Anna', 'Bob', 'Civic']),  # Multiple palindromes
            (['Anna', 'Bob', 'Civic', 'David', 'racecar'], ['Anna', 'Bob', 'Civic', 'racecar']),  # Additional palindrome
            ([], []),  # Empty list
        ]

        for names, expected in test_cases:
            with self.subTest(names=names):
                result = palindrome_names(names)
                self.assertEqual(result, expected,
                                 f"Palindrome filtering for {names} is incorrect. Expected: {expected}, Got: {result}")

    def test_make_words_to_count(self):
        test_cases = [
            ([], {}),  # Empty list
            (['abc'], {'abc': 1}),  # Only one word in list
            (['abc', 'def'], {'abc': 1, 'def': 1}),  # No duplicates in list
            (['abc', 'abc', 'abc'], {'abc': 3}),  # Only duplicates in list
            (['abc', 'def', 'abc', 'ghi'], {'abc': 2, 'def': 1, 'ghi': 1}),  # Mix of duplicates and non-duplicates
        ]

        for words, expected in test_cases:
            with self.subTest(words=words):
                result = make_words_to_count(words)
                self.assertEqual(result, expected,
                                 f"Word count for {words} is incorrect. Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    unittest.main()
