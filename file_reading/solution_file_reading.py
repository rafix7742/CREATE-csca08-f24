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

Example format: 
    [{'Name': 'JOHN DOE', 'Matched Cars': [{'Brand': 'Toyota', 'Model': 'Corolla', 'Price': 180000.0, 'Color': 'BLACK'}]}, 
    {'Name': 'JANE DOE', 'Matched Cars': [{'Brand': 'Honda', 'Model': 'Civic', 'Price': 200000.0, 'Color': 'RED'}]}, 
    {'Name': 'OLIVER SMITH', 'Matched Cars': []}, 
    {'Name': 'OLIVIA LOPEZ', 'Matched Cars': [{'Brand': 'Nissan', 'Model': 'Altima', 'Price': 240000.0, 'Color': 'GRAY'}, 
                                                {'Brand': 'Nissan', 'Model': 'Sentra', 'Price': 180000.0, 'Color': 'WHITE'}]}]

Notes:
    You are given constants for sepraating data from certain lines
    You may look at the data in "small_customers.txt"
'''
def parse_customers(file_name: str, car_database: dict) -> list:

    # List to store customer dictionaries
    customers = []

    # Open the file for reading
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Parse the customer data
    i = 0
    while i < len(lines):

        # Read customer name and budget
        customer_data = lines[i].strip().split(SEP)
        name = customer_data[0].strip()
        budget = float(customer_data[1].strip())
        i += 1

        # Read preferred brand
        brand = lines[i].strip()
        i += 1

        #####################################
        # Collect preferred colors - could be a helper
        preferred_colors = []
        while i < len(lines) and lines[i].strip() != END:
            preferred_colors.append(lines[i].strip())
            i += 1
        #####################################

        # Skip the "END" line
        i += 1

        # Match cars for the customer
        matched_cars = compare_cars(car_database, budget, preferred_colors, brand)

        # Append the customer's dictionary
        customers.append({"Name": name, "Matched Cars": matched_cars})

    return customers

def compare_cars(car_database: dict, budget: float, preferred_colors: list, brand: str) -> list:
    matched_cars = []

    # Standardize the brand name
    brand = brand.title()

    # Check if the brand exists in the car database
    if brand in car_database:
        # Loop through the models of the specified brand
        for model in car_database[brand]:
            # Extract the car's details
            car_details = car_database[brand][model]
            price = car_details[0]
            color = car_details[1].upper()
            for_sale = car_details[2]

            # Check if the car matches the criteria
            if price <= budget:
                if color in preferred_colors:
                    if for_sale:
                        # Add the car to the matched list
                        matched_cars.append({"Brand": brand, "Model": model, "Price": price, "Color": color})

    return matched_cars


# Load customer data and match cars
customer_matches = parse_customers("file_reading/small_customers.txt", CAR_DATABASE)
print(customer_matches)