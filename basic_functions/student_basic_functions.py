
from typing import Tuple



'''Write the docstring for the following function'''
def sum_and_multiply(nums: list[int]) -> int:
    total = 0
    multiplier = len(nums)
    for num in nums:
        total += num
    return num * multiplier



'''Write the docstring for the following function'''
def is_good_acedmic_standing(student: Tuple[str,float]) -> bool:
    return student[1] > 1.6


''' Write the docstring for the following function and implement it,
    the function name is literal in what it is asking you to implement
    I.e the greatest common denominator between num1 and num2
'''
def greatest_common_denominator(num1: int, num2: int) ->int:
    return

'''Write the doc string for this function and implement it 
We want the result to be a list of names that are palindromes,
this should not be case sensitive

Recall a palindrome is a string where it is the same as its reverse,
ex. Hannah is a palindrome, !@$@! is a palindrome, Banana is not a palindrome
 '''
def palindrome_names(names: list[str]) -> list:
    return



'''
The following function and question was taken from the Fall 2023 TT2,
the original question was split into two seprate questions, one for implementation
and one for testing.
You do not need to implement the function in order to create the minimal testing set.
See test_case.docx for the worksheet format.
These types of questions are very common.


Write the MINIMAL test set for this problem, do not have ANY redundant cases, you only need 5 total tests
AFTER writing te minimal test set, complete the implementation of this function 
(do not implement before writing the test set)
'''
def make_words_to_count(words: list[str]) -> dict[str,int]:
    """Returns a dictionary that maps each word to the numer of times it appears in words,
    >>> res = make_words_to_count(['abc','mme','abc','7'])
    >>> res = {'abc': 2,'mme': 1,'7':1}
    True

    """



'''
The following function and question was taken from the Fall 2023 EXAM,
You do not need to implement the function in order to create the minimal testing set.
See test_case.docx for the worksheet format.
These types of questions are very common.


Write the MINIMAL test set for this problem, do not have ANY redundant cases, you only need 6 total tests
you do not need to implement this function, only write its tests
'''
def contains_in_list(lst: list[int], item: int) -> bool:
    "Return true if and only if item appears in lst"
    return

