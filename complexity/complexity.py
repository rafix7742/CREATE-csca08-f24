"""CSCA08 Review Seminar (Nov 27th) by C.R.E.A.T.E. Club, time complexity questions

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.
"""

# Question 1
def search(lst: list[int], target: int) -> int:
    """ Return the index of the target in the list, if not found, return -1

    >>> search([1, 2, 3, 4], 3)
    2
    >>> search([1, 2, 3, 4], 5)
    -1
    """

    i = 0
    j = len(lst) - 1
    while i <= j:
        if lst[i] == target:
            return i
        if lst[j] == target:
            return j
        i = i + 1
        j = j - 1

    return -1

# Question 2
def partial_sum(lst: list[int]) -> list[int]:
    """ Return a list with same length as 'lst' in which each
    item in the output is the sum of respective item in 'lst'
    and anything came before it

    >>> partial_sum([1, 2, 3, 4])
    [1, 3, 6, 10]
    >>> partial_sum([1, 5, 2, 4, 5])
    [1, 6, 8, 12, 17]
    """

    result = []

    for i in range(len(lst)):
        result.append(lst[i])
        for j in range(i):
            result[-1] = result[-1] + lst[j]

    return result

# Question 3  
def find_pairs(lst: list[int], target: int) -> list[tuple[int, int]]:
    """ Return a list of all unique pairs of numbers from the input list that add up to the target sum.

    >>> find_pairs([1, 2, 3, 4, 5], 5)
    [(1, 4), (2, 3)]
    >>> find_pairs([1, 3, 2, 4, 1], 5)
    [(1, 4), (2, 3)]
    >>> find_pairs([1, 1, 1], 2)
    [(1, 1)]
    """

    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                if (lst[j], lst[i]) not in result: 
                    result.append((lst[i], lst[j])) #Ex: Why do we append like this?
    return result

if __name__ == '__main__':
    print(partial_sum([1, 2, 3, 4]))
    print(search([1, 2, 3, 3, 4], 3))
    print(find_pairs([1, 2, 3, 4, 5], 5))