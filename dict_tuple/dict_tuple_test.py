import math
from solution_dict_tuple import fastest_individual_category, fastest_total_time, get_total_time
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

def test_fastest_individual_category():
    print("Running tests for fastest_individual_category")
    # Test case: Fastest in Swimming
    category = "Swimming"
    expected = "Jennifer"
    result = fastest_individual_category(contestants, category)
    print(f"Test fastest_individual_category(contestants, 'Swimming'): Expected {expected}, Got {result}")
    assert result == expected

    # Test case: Fastest in Biking
    category = "Biking"
    expected = "Zangeif"
    result = fastest_individual_category(contestants, category)
    print(f"Test fastest_individual_category(contestants, 'Biking'): Expected {expected}, Got {result}")
    assert result == expected

    # Test case: Fastest in Running
    category = "Running"
    expected = "Zangeif"
    result = fastest_individual_category(contestants, category)
    print(f"Test fastest_individual_category(contestants, 'Running'): Expected {expected}, Got {result}")
    assert result == expected


def test_get_total_time():
    print("Running tests for get_total_time")
    # Test case: Total time for all contestants
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
    print(f"Test get_total_time(contestants): Expected {expected}, Got {result}")
    
    # this is a bit of a hacky solution but it handles any FP errors
    # For students going here and wonering what this is its basically
    # adding a tolerance for floating point arithmetic, it wont be on your exam
    # the addition for Steve's numbers cause this issue, to avoid it we add 
    # a tolerence 
    for (name_e, time_e), (name_r, time_r) in zip(expected, result):
        assert name_e == name_r, f"Names do not match: {name_e} != {name_r}"
        assert math.isclose(time_e, time_r), f"Times for {name_e} do not match: {time_e} != {time_r}"


def test_fastest_total_time():
    print("Running tests for fastest_total_time")
    # Test case: Fastest total time among all contestants
    expected = "Zangeif"
    result = fastest_total_time(contestants)
    print(f"Test fastest_total_time(contestants): Expected {expected}, Got {result}")
    assert result == expected


# Run all tests
def run_all_tests():
    test_fastest_individual_category()
    test_get_total_time()
    test_fastest_total_time()
    print("All tests passed successfully!")


run_all_tests()
