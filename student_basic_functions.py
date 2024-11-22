
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



'''Write the MINIMAL test set for this problem, do not have ANY redundant cases, you only need 5 total tests
AFTER writing te minimal test set, complete the implementation of this function 
(do not implement before writing the test set)
'''
def make_words_to_count(words: list[str]) -> dict[str,int]:
    """Returns a dictionary that maps each word to the numer of times it appears in words,
    >>> res = make_words_to_count(['abc','mme','abc','7'])
    >>> res = {'abc': 2,'mme': 1,'7':1}
    True

    """



'''Write the MINIMAL test set for this problem, do not have ANY redundant cases, you only need 6 total tests
you do not need to implement this function, only write its tests
'''
def contains_in_list(lst: list[int], item: int) -> bool:
    "Return true if and only if item appears in lst"
    return

'''Help! we dropped our compare nums function on its head! this has scrammbled its if else logic
    We need you to refactor this function to properly compare numbers like it used to, it has 
    wacky rules in place though


    Rules:
    1. If we have the same number, we return -7
    2. If we have num1 = 0, and num2 is any number we return 4
    3. If we have num2 = 0 and num 1 is any number we return 8
    4. If both num1 and num2 are 0, we return 328
    5. If both num1 and num2 are negative we return 9
    6. If either num1 or num2 are negative return 12
    7. Otherwise we return 0


    Your responsibility is to refactor this code to have the correct if/else logic,
    for those wondering when we will ever need to use a function like this, we wont,
    this is really good practice for understanding if else logic
    Hint: you may find it useful to determine rule priority before refactoring

'''
def wacky_compare_nums(num1: int, num2: int) -> int:
    if num1 < 0 or num2 < 0:  
        return 12
    elif num1 < 0 and num2 < 0:  
        return 9
    elif num1 == 0:  
        return 4
    elif num1 == num2:  
        return -7
    elif num1 == 0 and num2 == 0:  
        return 328
    elif num2 == 0:  
        return 8
    return 0