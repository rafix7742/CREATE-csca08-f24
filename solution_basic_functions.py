
from typing import Tuple



'''Need to come back and write docstrings'''
def sum_and_multiply(nums: list[int]) -> int:
    total = 0
    multiplier = len(nums)
    for num in nums:
        total += num
    return num * multiplier



'''Need to come back and write docstrings'''
def is_good_acedmic_standing(student: Tuple[str,float]) -> bool:
    return student[1] > 1.6


''' Need to come back and write docstrings'''
def greatest_common_denominator(num1: int, num2: int) ->int:

    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return abs(num1)


'''Need to come back and write docstrings'''
def palindrome_names(names: list[str]) -> list:

    name_list = []
    ## Alternate solution
    ## I dont expect anyone to get this but it is a really nice trick with string splicing
    # for name in names:
    #     if name.lower() == name.lower()[::-1]:
    #         name_list.append(name)
    # return name_list

    for name in names:
        # lower case and create the reverse name
        lower_name = name.lower()
        reversed_name = ""
        index = len(lower_name) - 1
        while index >= 0:
            reversed_name += lower_name[index]
            index -= 1
        # if they're equal, great add it to the list
        if lower_name == reversed_name:
            name_list.append(name)

    return name_list








