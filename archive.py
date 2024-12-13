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


def soln_wacky_compare_nums(num1: int, num2: int) -> int:
    if num1 == 0 and num2 == 0:  # Rule 4
        return 328
    elif num1 < 0 and num2 < 0:  # Rule 5
        return 9
    elif num1 < 0 or num2 < 0:  # Rule 6
        return 12
    elif num1 == num2:  # Rule 1
        return -7
    elif num1 == 0:  # Rule 2
        return 4
    elif num2 == 0:  # Rule 3
        return 8
    return 0
