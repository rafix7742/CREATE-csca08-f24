from solution_basic_functions import greatest_common_denominator, make_words_to_count, palindrome_names



def test_greatest_common_denominator():
    print("Running tests for greatest_common_denominator")
    # Test case: Common denominator exists
    num1, num2 = 8, 12
    expected = 4
    result = greatest_common_denominator(num1, num2)
    print(f"Test greatest_common_denominator(8, 12): Expected {expected}, Got {result}")
    assert result == expected

    # Test case: One number is a multiple of the other
    num1, num2 = 9, 3
    expected = 3
    result = greatest_common_denominator(num1, num2)
    print(f"Test greatest_common_denominator(9, 3): Expected {expected}, Got {result}")
    assert result == expected

    # Test case: No common denominators other than 1
    num1, num2 = 7, 13
    expected = 1
    result = greatest_common_denominator(num1, num2)
    print(f"Test greatest_common_denominator(7, 13): Expected {expected}, Got {result}")
    assert result == expected


def test_palindrome_names():
    print("Running tests for palindrome_names")
    # Test case: List with multiple palindromes
    names = ['Anna', 'Bob', 'Civic', 'David']
    expected = ['Anna', 'Bob', 'Civic']
    result = palindrome_names(names)
    print(f"Test palindrome_names(['Anna', 'Bob', 'Civic', 'David']): Expected {expected}, Got {result}")
    assert result == expected

    # Test case: List with additional palindrome
    names = ['Anna', 'Bob', 'Civic', 'David', 'racecar']
    expected = ['Anna', 'Bob', 'Civic', 'racecar']
    result = palindrome_names(names)
    print(f"Test palindrome_names(['Anna', 'Bob', 'Civic', 'David', 'racecar']): Expected {expected}, Got {result}")
    assert result == expected

    # Test case: Empty list
    names = []
    expected = []
    result = palindrome_names(names)
    print(f"Test palindrome_names([]): Expected {expected}, Got {result}")
    assert result == expected


def test_make_words_to_count():
    print("Running tests for make_words_to_count")
    # Test case: Normal list with repeated words
    words = ['abc', 'mme', 'abc', '7']
    expected = {'abc': 2, 'mme': 1, '7': 1}
    result = make_words_to_count(words)
    print(f"Test make_words_to_count(['abc', 'mme', 'abc', '7']): Expected {expected}, Got {result}")
    assert result == expected

    # Test case: List with unique words
    words = ['a', 'b', 'a']
    expected = {'a': 2, 'b': 1}
    result = make_words_to_count(words)
    print(f"Test make_words_to_count(['a', 'b', 'a']): Expected {expected}, Got {result}")
    assert result == expected

    # Test case: Empty list
    words = []
    expected = {}
    result = make_words_to_count(words)
    print(f"Test make_words_to_count([]): Expected {expected}, Got {result}")
    assert result == expected


# Run all tests
def run_all_tests():
    test_greatest_common_denominator()
    test_palindrome_names()
    test_make_words_to_count()
    print("All tests passed successfully!")


run_all_tests()
