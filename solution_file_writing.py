


from typing import TextIO

'''
Helper function, i will write proper docstrings later
'''
def parse_cars_data(cars_dict: dict) -> list:

    cars_list = []
    for car_brand in cars_dict:
        #split the car brands into their models
        models = cars_dict[car_brand]
        for car_model in models:
            # split models into specific cars and parse
            # note that car_model is a key, NOT an index
            car_details = models[car_model]
            #build the new dicts  
            car_data = {
                'brand': car_brand,
                'model': car_model,
                'price': car_details[0],
                'color': car_details[1],
                'isforsale': car_details[2]
            }
            cars_list.append(car_data)

    return cars_list

''' Helper function, i will write proper doc strings later'''
def format_cars_for_sale(cars_dict: dict) -> list:
    #use helper to parse the data to make it easier to work with
    cars_list = parse_cars_data(cars_dict)
    formatted_list = []
    # itterate over the cars and check if its for sale
    for car in cars_list:
        if car['isforsale']:
            # add all for sale cars to a list of strings to print in the main function
            formatted_list.append(
                f'This car is a {car["color"]} {car["brand"]} {car["model"]}, it costs ${car["price"]}.'
            )
    return formatted_list


'''Will come back and write proper docstring

'''
def write_cars_for_sale_to_file(cars_dict: dict, file_path: TextIO) -> None:


    formatted_cars = format_cars_for_sale(cars_dict)
    
    with open(file_path, 'w') as file:
        index = 0
        while index < len(formatted_cars):
            #simply go over all the for sale cars and print them out 
            # we have already formatted the strings so no more work is needed
            file.write(formatted_cars[index] + '\n')
            index += 1