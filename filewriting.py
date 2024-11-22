
from typing import List, TextIO, Tuple


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


'''Write the doc string for this function and implement it 
We want the result to be a list of names that are palindromes,
this should not be case sensitive '''
def palindrome_names(names: List[str]) -> list:

    name_list = []
    # Alternate solution\
    # I dont expect anyone to get this but it is a really nice trick with string splicing
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
    



'''
Parses a nested dictionary into a list of car dictionaries.

:param cars_dict: Nested dictionary with the structure:
                    {car_brand: {car_model: (price, color, isforsale)}}
:return: List of dictionaries, each representing a car.
'''
def parse_cars_data(cars_dict: dict) -> list:

    cars_list = []
    for car_brand in cars_dict:
        models = cars_dict[car_brand]
        for car_model in models:
            car_details = models[car_model]  
            car_data = {
                'brand': car_brand,
                'model': car_model,
                'price': car_details[0],
                'color': car_details[1],
                'isforsale': car_details[2]
            }
            cars_list.append(car_data)

    return cars_list

'''
    Formats the list of car dictionaries into strings for cars that are for sale.

    :param cars_list: List of dictionaries, each representing a car.
    :return: List of formatted strings for cars that are for sale.
    '''
def format_cars_for_sale(cars_dict: dict) -> list:
    
    cars_list = parse_cars_data(cars_dict)
    formatted_list = []
    for car in cars_list:
        if car['isforsale']:
            formatted_list.append(
                f'This car is a {car["color"]} {car["brand"]} {car["model"]}, it costs ${car["price"]}.'
            )
    return formatted_list





def write_cars_for_sale_to_file(cars_dict: dict, file_path: TextIO) -> None:
    '''
    Writes information about cars for sale to a file using a while loop.

    :param cars_dict: Nested dictionary with the structure:
                      {car_brand: {car_model: (price, color, isforsale)}}
    :param file_path: Path to the file where the output will be written.
    '''

    formatted_cars = format_cars_for_sale(cars_dict)
    
    with open(file_path, 'w') as file:
        index = 0
        while index < len(formatted_cars):
            file.write(formatted_cars[index] + '\n')
            index += 1


cars = {
    'Toyota': {
        'Camry': (30000, 'red', True),
        'Corolla': (20000, 'blue', False),
    },
    'Honda': {
        'Civic': (25000, 'black', True),
        'Accord': (27000, 'white', True),
    },
    'Ford': {
        'Mustang': (55000, 'yellow', False),
        'Fiesta': (15000, 'green', True),
    },
}

write_cars_for_sale_to_file(cars, 'cars_for_sale.txt')





'''Returns the float result. Takes in exp: Tuple[float,int] where our first parameter is the base,
and the second is the exponent, our exponent is non-negative.
We return -1 when the exponent is negative, or -2 if we are in an indeterminate form (recall MATA31)
write out the description of a minimal testing set as provided in "insert file name"
You do not need more tests than what is provided.
You may find it easier to implement first and then write test descriptions.


Hint: Remember what non-negative means and notice that base can be negative.

While implementing do NOT use the pow() or ** operator for your solution.
yes these work but it is not the intention of the problem, you must use itteration.

Bonus exercise: write the doc string for this function
'''
def simple_exponent(exp: Tuple[float,int]) -> float:
    # order of checks does matter
    # only indeterminant form
    if(exp[0] == 0 and exp[1]==0):
        return -2
    # Two cases of base or exponent being negative
    elif(exp[0] == 0):
        return 0
    elif(exp[1] == 0):
        return 1
    idx = 0
    # if we are here we can run the loop normally
    result = exp[0]
    while(exp[1] > idx):
        result = result*exp[0]
        idx += 1
    # returns a float as base may be negative 
    return result



CATEGORIES = ["Swimming","Biking", "Running"]
BIG_NUMBER = 999999999
contestants = {
    "Alice": [("Swimming", 15.22 ), ("Biking", 12.33),("Running", 10.59)],
    "Bob": [("Swimming", 8.21), ("Biking", 9.23),("Running", 8.56)],
    "Charlie": [("Swimming", 10.33), ("Biking", 13.22),("Running", 7.35)],
    "Dave": [("Swimming", 6.36), ("Biking", 8.43),("Running", 14.32)],
    "Steve": [("Swimming", 7.46), ("Biking", 9.34),("Running", 9.33)],
    "Marley": [("Swimming", 8.41), ("Biking", 10.57),("Running", 9.32)],
    "Zangeif": [("Swimming", 8.21), ("Biking", 4.36),("Running", 6.11)],
    "Jennifer": [("Swimming",5.42), ("Biking", 8.59),("Running", 9.41)]
}


def fastest_individual_category(contestants: dict, category: str) -> str:
    
    if category not in CATEGORIES:
        return "N/A"

    fastest_contestant = ""
    fastest_time = BIG_NUMBER

    contestant_names = list(contestants.keys())
    i = 0
    while i < len(contestant_names):
        contestant = contestant_names[i]
        events = contestants[contestant]

        j = 0
        while j < len(events):
            event_category, time = events[j]
            if event_category == category and time < fastest_time:
                fastest_time = time
                fastest_contestant = contestant
            j += 1

        i += 1

    return fastest_contestant


''' Complete the following helper function for fastest total time and provide a valid doc string

    To get you started, notice that the return type is list[Tuple], take a look at how the above 
    function will use this helper function 

'''
def get_total_time(contestants: dict) -> list[Tuple]:
    times = []
    contestant_names = list(contestants.keys())
    i = 0
    while i < len(contestant_names):
        contestant = contestant_names[i]
        events = contestants[contestant]

        total_time = 0
        j = 0
        while j < len(events):
            time = events[j][1]
            total_time += time
            j += 1

        times.append((contestant, total_time))
        i += 1

    return times

'''Create the docstring for this function'''
def fastest_total_time(contestants: dict) -> str:



    #Helper function to be created below
    total_times = get_total_time(contestants)
    #Helper function to be created below

    smallest_time = BIG_NUMBER
    fastest_contestant = ""

    idx = 0
    while idx < len(total_times):
        contestant = (total_times[idx][0],total_times[idx][1])
        if contestant[1] < smallest_time:
            smallest_time = contestant[1]
            fastest_contestant = contestant[0]
        idx += 1

    return fastest_contestant 


print(fastest_total_time(contestants))


