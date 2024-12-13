import unittest
import math
from solution_dict_tuple import fastest_individual_category, fastest_total_time, get_total_time

contestants = {
    "Alice": [("Swimming", 15.22), ("Biking", 12.33), ("Running", 10.59)],
    "Bob": [("Swimming", 8.21), ("Biking", 9.23), ("Running", 8.56)],
    "Charlie": [("Swimming", 10.33), ("Biking", 13.22), ("Running", 7.35)],
    "Dave": [("Swimming", 6.36), ("Biking", 8.43), ("Running", 14.32)],
    "Steve": [("Swimming", 7.46), ("Biking", 9.34), ("Running", 9.33)],
    "Marley": [("Swimming", 8.41), ("Biking", 10.57), ("Running", 9.32)],
    "Zangeif": [("Swimming", 8.21), ("Biking", 4.36), ("Running", 6.11)],
    "Jennifer": [("Swimming", 5.42), ("Biking", 8.59), ("Running", 9.41)]
}


class TestTriathlonFunctions(unittest.TestCase):

    def test_fastest_individual_category(self):
        test_cases = [
            ("Swimming", "Jennifer"),
            ("Biking", "Zangeif"),
            ("Running", "Zangeif")
        ]

        for category, expected in test_cases:
            with self.subTest(category=category):
                result = fastest_individual_category(contestants, category)
                self.assertEqual(result, expected,
                                 f"Fastest individual in category '{category}' is incorrect. Expected: {expected}, Got: {result}")

    def test_get_total_time(self):
        expected = [
            ('Alice', 38.14),
            ('Bob', 26.0),
            ('Charlie', 30.9),
            ('Dave', 29.11),
            ('Steve', 26.13),
            ('Marley', 28.3),
            ('Zangeif', 18.68),
            ('Jennifer', 23.42)
        ]

        result = get_total_time(contestants)
        # do not worry about this, this handles floating point errors
        # something like this is not tested for A08, it is just to make testing
        # easier to deal with instead of changing the data
        # Pretty hacky solution but oh well
        for (name_e, time_e), (name_r, time_r) in zip(expected, result):
            with self.subTest(contestant=name_e):
                self.assertEqual(name_e, name_r, f"Contestant names do not match: {name_e} != {name_r}")
                self.assertTrue(math.isclose(time_e, time_r),
                                f"Total times for {name_e} do not match: {time_e} != {time_r}")

    def test_fastest_total_time(self):
        expected = "Zangeif"
        result = fastest_total_time(contestants)
        self.assertEqual(result, expected,
                         f"Fastest total time contestant is incorrect. Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    unittest.main()
