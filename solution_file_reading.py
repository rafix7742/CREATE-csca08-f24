from typing import TextIO

from cars_db import CAR_DATABASE


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
END = "END"  # Marks the end of each customer's record
SEP = ";"  # Separator for the customer data

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

The function will:
    Read and parse the file. Assume that the file is already open.
    Match customers with cars within their budget and preferred color(s).
    Return a list of dictionaries 'customers' representing each customer and their potential cars.


Notes:
    You are given constants for sepraating data from certain lines
    You may look at the data in "insert file name"
'''
def parse_customers(data_file: TextIO, car_database: dict) -> list:

    # List to store customer dictionaries
    customers = []

    with open(data_file, 'r') as file:
        lines = file.readlines()

    # Parse the customer data
    i = 0
    while i < len(lines):

        # Split the current line into name and budget
        customer_data = lines[i].split(SEP)
        name = customer_data[0].strip()
        budget = int(customer_data[1].strip())
        brand = lines[i+1].strip()
        

        ###########################
        # could probably be a helper
        # Get the preferred colors (can be one or more colors)
        preferred_colors = []
        i += 1
        while i < len(lines) and lines[i] != END:
            preferred_colors.append(lines[i].strip())  # Add color to the list
            i += 1
        ###########################
        
        # Find matching cars for the customer
        matched_cars = compare_cars(car_database, budget, preferred_colors, brand)

        # Append the customer's dictionary
        customers.append({"Name": name, "Matched Cars": matched_cars})

        # Skip the "END" line
        i += 1

    return customers


def compare_cars(car_database: dict, budget: float, preferred_colors: list, brand: str) -> list:
    matched_cars = []
    # get all of the brands
    for brands in car_database.keys():
        #get all of the models of a specific brand
        for model in car_database[brands].keys(): 
            # we use key,key,idx for the brand,model and then the price or colour
            price = car_database[brands][model][0]
            car_color = car_database[brands][model][1]

            # Check if the car's price is within the budget and the color is one of the preferred colors
            if price <= budget and car_color in preferred_colors and brands.lower() == brand.lower():
                matched_cars.append({"Brand": brand, "Model": model})

    return matched_cars