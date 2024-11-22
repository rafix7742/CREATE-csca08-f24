from typing import Tuple


CATEGORIES = ["Swimming","Biking", "Running"]
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

''' Need to create doc string'''
def fastest_individual_category(contestants: dict, category: str) -> str:
 
    # get an empty string for the contestant 
    fastest_contestant = ""
    fastest_time = BIG_NUMBER

    # Iterate through each contestant
    for contestant_name in contestants:
        # get the event tuples for each person
        events = contestants[contestant_name]
        for event in events:
            #get the event category
            event_category = event[0]
            #get the time they had for that event
            time = event[1]
            # if the category is the same and the time is the newest low, 
            # store the time and name, otherwise continue
            if event_category.lower() == category.lower() and time < fastest_time:
                fastest_time = time
                fastest_contestant = contestant_name

    return fastest_contestant

''' Need to create docstring'''
def get_total_time(contestants: dict) -> list[Tuple]:

    times = []
    # get list of all contestant names (keys for later)
    contestant_names = list(contestants.keys())
    i = 0
    while i < len(contestant_names):
        # get the contestant individually to use as a key for events
        contestant = contestant_names[i]
        events = contestants[contestant]

        total_time = 0
        j = 0
        while j < len(events):
            # start summing the time of the contestant
            time = events[j][1]
            total_time += time
            j += 1
        # append their name and time in a list of tuples
        times.append((contestant, total_time))
        i += 1

    return times


'''Need to create docstring'''
def fastest_total_time(contestants: dict) -> str:

    #Helper function to be created above
    total_times = get_total_time(contestants)
    #Helper function to be created above

    smallest_time = BIG_NUMBER
    fastest_contestant = ""

    idx = 0
    while idx < len(total_times):
        contestant = (total_times[idx][0],total_times[idx][1])
        if contestant[1] < smallest_time:
            smallest_time = contestant[1]
            fastest_contestant = contestant[0]
        idx += 1

    return fastest_contestant 
