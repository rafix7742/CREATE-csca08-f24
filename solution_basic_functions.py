from typing import Tuple

'''Return the product of the last element of nums and the length of nums.
    >>> sum_and_multiply([1, 2, 3])
    9
    >>> sum_and_multiply([5])
    5
'''
def sum_and_multiply(nums: list[int]) -> int:
    total = 0
    multiplier = len(nums)
    for num in nums:
        total += num
    return num * multiplier



'''Return if tuple student (name, GPA) has a GPA greater than 1.6.
    >>> is_good_acedmic_standing(('Alice', 2.0))
    True
    >>> is_good_acedmic_standing(('Bob', 1.5))
    False
'''
def is_good_acedmic_standing(student: Tuple[str,float]) -> bool:
    return student[1] > 1.6


''' Return the greatest common denominator of num1 and num2.
    >>> greatest_common_denominator(8, 12)
    4
    >>> greatest_common_denominator(9, 3)
    3
'''
def greatest_common_denominator(num1: int, num2: int) ->int:

    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return abs(num1)


'''Return the items in the list names that are palindromes.
    >>> palindrome_names(['Anna', 'Bob', 'Civic', 'David'])
    ['Anna', 'Bob', 'Civic']
    >>> palindrome_names(['Anna', 'Bob', 'Civic', 'David', 'racecar'])
    ['Anna', 'Bob', 'Civic', 'racecar']
'''
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

'''Return a dictionary that maps each word in words to the numer of times it appears in words.
    >>> res = make_words_to_count(['abc','mme','abc','7'])
    res = {'abc': 2,'mme': 1,'7':1}
    >>> make_words_to_count(['a', 'b', 'a'])
    {'a': 2, 'b': 1}
'''
def make_words_to_count(words: list[str]) -> dict[str,int]:
    word_count = {}
    # go over each word
    for word in words:
        #check if word is already in our dict
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count





