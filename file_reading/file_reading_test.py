import unittest
from tempfile import NamedTemporaryFile
from solution_file_reading import parse_customers, compare_cars
from cars_db import CAR_DATABASE


class TestCarMatching(unittest.TestCase):

    def test_compare_cars_exact_match(self):
        budget = 250000.0
        preferred_colors = ["BLACK", "RED"]
        brand = "Toyota"
        
        matched_cars = compare_cars(CAR_DATABASE, budget, preferred_colors, brand)

        expected_result = [
            {"Brand": "Toyota", "Model": "Corolla", "Price": 180000.0, "Color": "BLACK"},
        ]
        self.assertEqual(matched_cars, expected_result)

    def test_compare_cars_no_match(self):
        budget = 150000.0
        preferred_colors = ["WHITE"]
        brand = "Honda"
        
        matched_cars = compare_cars(CAR_DATABASE, budget, preferred_colors, brand)

        self.assertEqual(matched_cars, [])

    def test_compare_cars_multiple_matches(self):
        budget = 300000.0
        preferred_colors = ["RED", "BLACK"]
        brand = "Honda"
        
        matched_cars = compare_cars(CAR_DATABASE, budget, preferred_colors, brand)

        expected_result = [
            {"Brand": "Honda", "Model": "Civic", "Price": 200000.0, "Color": "RED"},
            {"Brand": "Honda", "Model": "Accord", "Price": 300000.0, "Color": "BLACK"}
        ]
        self.assertEqual(matched_cars, expected_result)

    def test_parse_customers_valid_file(self):
        customer_data = """JOHN DOE; 200000;
Toyota
BLACK
END
JANE DOE; 250000;
Honda
BLACK
END
"""
        with NamedTemporaryFile('w', delete=False) as temp_file:
            temp_file.write(customer_data)
            temp_file_name = temp_file.name

        customers = parse_customers(temp_file_name, CAR_DATABASE)

        expected_result = [
            {'Name': 'JOHN DOE', 'Matched Cars': [{'Brand': 'Toyota', 'Model': 'Corolla', 'Price': 180000.0, 'Color': 'BLACK'}]},
            {'Name': 'JANE DOE', 'Matched Cars': []}
        ]

        self.assertEqual(customers, expected_result)

    def test_parse_customers_no_match(self):
        customer_data = """OLIVER SMITH; 100000; YELLOW
Ford
END
"""
        with NamedTemporaryFile('w', delete=False) as temp_file:
            temp_file.write(customer_data)
            temp_file_name = temp_file.name

        customers = parse_customers(temp_file_name, CAR_DATABASE)

        expected_result = [{'Name': 'OLIVER SMITH', 'Matched Cars': []}]
        self.assertEqual(customers, expected_result)

if __name__ == '__main__':
    unittest.main()
