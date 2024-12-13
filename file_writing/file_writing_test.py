import unittest
from typing import TextIO
from tempfile import NamedTemporaryFile

from solution_file_writing import write_cars_for_sale_to_file

Small_car_db = {
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

class TestCarsFunctions(unittest.TestCase):

    def test_write_cars_for_sale_to_file(self):
        expected_file_content = [
            "This car is a Black Toyota Corolla, it costs $180000.0.",
            "This car is a Black Toyota RAV4, it costs $270000.0.",
            "This car is a Red Honda Civic, it costs $200000.0.",
            "This car is a Black Honda Accord, it costs $300000.0.",
            "This car is a Yellow Honda CRV, it costs $350000.0.",
            "This car is a Black Ford Focus, it costs $150000.0.",
            "This car is a Red Ford Escape, it costs $200000.0.",
        ]

        with NamedTemporaryFile(mode='r+', delete=False) as temp_file:
            write_cars_for_sale_to_file(Small_car_db, temp_file.name)
            temp_file.seek(0)
            file_content = temp_file.readlines()

        for idx, line in enumerate(file_content):
            expected_line = expected_file_content[idx] + "\n"
            with self.subTest(line_number=idx + 1):
                self.assertEqual(line, expected_line, f"Mismatch at line {idx + 1}: Expected '{expected_line}', got '{line}'")

if __name__ == "__main__":
    unittest.main()


