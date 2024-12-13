from typing import TextIO

END = "END"  # Marks the end of each customer's record
SEP = ";"  # Separator for the customer data

car_sample_database = {
        "Toyota": {
            "Corolla": (180000.0, "BLACK", True),
            "Camry": (250000.0, "RED", False),
            "RAV4": (270000.0, "BLACK", True),
        },
        "Honda": {
            "Civic": (200000.0, "RED", True),
            "Accord": (300000.0, "BLACK", True),
            "CRV": (350000.0, "YELLOW", True),
        },
        "Ford": {
            "Focus": (150000.0, "BLACK", True),
            "Escape": (200000.0, "RED", True),
            "Explorer": (500000.0, "YELLOW", False),
        },
    }
''' 
File Structure and Data Parsing:

Input File (customers.txt): 
    Contains customer data in the format:
    Name (String)
    Budget (Integer)
    Preferred Color (String)
    END to mark the end of each customer's record.

Dictionary Structure:
    Outer Dictionary: Car brands (e.g., "Toyota", "Honda").
    Inner Dictionary: Car models belonging to a specific brand.
    Tuple: Contains the price (float), available color (string), and forSale (boolean).
    For additonal context, see the above car_sample_database

The function will:
    Read and parse the file. Assume that the file is already open.
    Match customers with cars within their budget and preferred color(s).
    Return a list of dictionaries 'customers' representing each customer and their potential cars.

Hint: you may find it useful to write a helper or two for this function
'''

def parse_customers(data_file: TextIO, car_database: dict) -> list:
    return