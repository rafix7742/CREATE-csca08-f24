
from typing import List, TextIO, Tuple

car_sample_database = {
        "Toyota": {
            "Corolla": (180000.0, "Black", True),
            "Camry": (250000.0, "Red", False),
            "RAV4": (270000.0, "Black", True),
        },
        "Honda": {
            "Civic": (200000.0, "Red", True),
            "Accord": (300000.0, "Black", True),
            "CRV": (350000.0, "Yellow", True),
        },
        "Ford": {
            "Focus": (150000.0, "Black", True),
            "Escape": (200000.0, "Red", True),
            "Explorer": (500000.0, "Yellow", False),
        },
    }


'''Write a valid docstring for this function, 

Dictionary Structure:
    Outer Dictionary: Car brands (e.g., "Toyota", "Honda").
    Inner Dictionary: Car models belonging to a specific brand.
    Tuple: Contains the price (float), available color (string), and isForSale (boolean).
    For additonal context, see the above car_sample_database


Goal: write to a file with car information for all cars that are avaliable for sale
each line should be in the format of the following: 
This car is a "color" "brand" "model", it costs $"price" 


You may find it useful to write helper functions for this 
The file is open for writing, you do not need to read data from a file for this function
a smaller version of the dictionary will be provided above for your reference

Any helper functions you create it is good practice to also write docstrings for them as well
'''
def write_cars_for_sale_to_file(cars_dict: dict, file_path: TextIO) -> None:
    with open(file_path, 'w') as file:
        print("this is a file at")
    return