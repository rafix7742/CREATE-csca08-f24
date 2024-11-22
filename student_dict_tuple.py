
from typing import Tuple


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


''' Write a valid doc string for this function, we want to return the name of 
    who has the fastest time for ANY given category, if we have no contestants, 
    return an empty string

    You may assume that the categories are either Swimming, Biking or Running
    You do not need to worry about case sensitivity, you may assume valid input
    for the category, i.e all contestants will have done all three events

'''
def fastest_individual_category(contestants: dict, category: str) -> str:
    return


''' Complete the following helper function for fastest total time and provide a valid doc string

    To get you started, notice that the return type is list[Tuple], take a look at how the below 
    function will use this helper function

    Hint: We want to get a list of each conestants total times, how can we do this?

'''
def get_total_time(contestants: dict) -> list[Tuple]:
    return


'''Create the docstring for this function'''
def fastest_total_time(contestants: dict) -> str:



    #Helper function to be created above
    contestant_total_times = get_total_time(contestants)
    #Helper function to be created above

    smallest_time = BIG_NUMBER
    fastest_contestant = ""

    idx = 0
    while idx < len(contestant_total_times):
        contestant = (contestant_total_times[idx][0],contestant_total_times[idx][1])
        if contestant[1] < smallest_time:
            smallest_time = contestant[1]
            fastest_contestant = contestant[0]
        idx += 1

    return fastest_contestant