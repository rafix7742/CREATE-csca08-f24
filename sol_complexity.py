"""CSCA08 Review Seminar (Nov 27th) by C.R.E.A.T.E. Club, time complexity questions

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.
"""

# Solution 1
def search(lst: list[int], target: int) -> int:
    """ Return the index of the target in the list lst, if not found, return -1

    >>> search([1, 2, 3, 4], 3)
    2
    >>> search([1, 2, 3, 4], 5)
    -1
    """

    # Tip: before you start calculating, make sure that you can understand what the algorithm is doing
    #      If you cannot, visualize the algorithm with a simple example

    i = 0
    j = len(lst) - 1 # indexes of the first and last elements
    while i <= j:
        if lst[i] == target:
            return i # if the target is found at the beginning
        if lst[j] == target:
            return j # if the target is found at the end
        i = i + 1 
        j = j - 1 # i and j are getting closer to each other

    return -1 
    # this algo searches for a given target in the list. it traverses the entire list.
    # thus, the time complexity is O(n) where n is the length of the list
    # the best case is O(1), which is if the target is at the beginning or the end of the list


# Solution 2
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

    for i in range(len(lst)): #runs n times
        result.append(lst[i]) #takes O(1) time
        for j in range(i): #runs i times where i is the index of the outer loop
            result[-1] = result[-1] + lst[j] #takes O(1) time

    return result
    # this algo calculates the partial sum of the list. it traverses the entire list.
    # in total, the outer for loop will run n times
    # inner for loop will run 1 + 2 + 3 + .... (n-1) times, which is equal to n(n-1)/2 => ( n^2 - n ) / 2 => O(n^2)
    # think about: why is the time complexity O(n^2) and not O(n^3)? When would the time complexity be O(n^3)?

# Solution 3  
def find_pairs(lst: list[int], target: int) -> list[tuple[int, int]]:
    """ Return a list of all unique pairs of numbers from the input list lst that add up to the target sum.

    >>> find_pairs([1, 2, 3, 4, 5], 5)
    [(1, 4), (2, 3)]
    >>> find_pairs([1, 3, 2, 4, 1], 5)
    [(1, 4), (2, 3)]
    >>> find_pairs([1, 1, 1], 2)
    [(1, 1)]
    """

    result = []
    for i in range(len(lst)): #runs n times where n is the length of the list
        for j in range(i + 1, len(lst)): # runs n - i - 1 times
            if lst[i] + lst[j] == target: #takes O(1) time
                if (lst[j], lst[i]) not in result: 
                    result.append((lst[i], lst[j])) #To avoid duplicates #takes O(1) time
    return result
    # Does this look familiar? this algo finds all the unique pairs of numbers that add up to the target sum.
    # in total, the outer for loop will run n times
    # inner for loop will run n - 1 times for the first iteration, n - 2 times for the second iteration, and so on. n-1 + n-2 + n-3 + ... + 1 = n(n-1)/2 => O(n^2)
    # similar to the question above, think about: why is the time complexity O(n^2) and not O(n^3)? When would the time complexity be O(n^3)?

if __name__ == '__main__':
    print(partial_sum([1, 2, 3, 4]))
    print(search([1, 2, 3, 3, 4], 3))
    print(find_pairs([1, 2, 3, 4, 5], 5))