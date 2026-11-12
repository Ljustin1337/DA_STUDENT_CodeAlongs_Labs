#!/usr/bin/env python3
"""Meet the Objects: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "/Users/jlee333/Desktop/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/meet-the-objects/bike_stations.json"  # edit the filepath with the data

with open(DATA_FILE) as f:
    stations = json.load(f)


# ===== Day 1 =====

# Step 1: Reproduce the Parallel-List Bug and Name the Wrong Stations
# TODO: assign `names` and `bikes` to two empty lists
names = []
bikes = []
# TODO: loop over `stations`; append each one's "name" to `names`
for station in stations: 
    names.append(station["name"])
# TODO: append the same station's "bikes_available" to `bikes`
    bikes.append(station["bikes_available"])


names.pop(2)

print("stations in the file:", len(stations))
# TODO: loop over range(len(names)); print names[i], "|", bikes[i], "bikes"

for i in range(len(names)):
    print(names[i], "|", bikes[i], "bikes")

# Step 1, answer 1:
#
# Step 1, answer 2:
#
# Step 1, answer 3:
#


# Step 2: Define the Station Class and Prove Two Instances Are Independent
class Station:
    # TODO: add __init__ with name (str), capacity and bikes_available (int)
    def __init__(self, name , capacity, bikes_available, needs_maintenance, station_id ):

    # TODO: in __init__, assign each parameter to self.<same name>
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance
        self.station_id = station_id
    # TODO: add a parameter and self.<name> for each extra field you agreed
    
    # TODO: add needs_restock(self): True if bikes_available < capacity / 4
    def needs_restock(self):
        """if self.bikes_available < self.capacity/4:
            return True
        else:
            return False"""
        return self.bikes_available < self.capacity/4
    def __str__(self):
        return f"{self.name}:{self.bikes_available} of {self.capacity} bikes"

# TODO: assign `fleet` to []; loop over `stations` as `s`

fleet = []

for s in stations:
# TODO: append Station(s["name"], s["capacity"], s["bikes_available"])
    fleet.append(Station(s["name"], s["capacity"], s["bikes_available"], s["station_id"], s["needs_maintenance"]))
# TODO: assign `busy`, `quiet` to two stations with equal needs_restock()
busy = fleet[1]
quiet = fleet[-1]

# TODO: print both needs_restock() answers
print(busy.needs_restock(), quiet.needs_restock())
# TODO: set busy.bikes_available to 0, then print both answers again
busy.bikes_available = 0 

print("after:", busy.needs_restock(), quiet.needs_restock())
# Step 2, answer 1:
#
# Step 2, answer 2:
#
# Step 2, answer 3:
#
# Step 2, answer 4:
#


# ===== Day 2 =====

# Step 3: Add `__str__` and Find Out Which of Four Prints It Changes
print(fleet[0])
print(fleet[:2])


# TODO: copy your Station class from Step 2 here
class Station:
    def __init__(self, name , capacity, bikes_available, needs_maintenance, station_id ):

        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance
        self.station_id = station_id
    
    def needs_restock(self):
        if self.bikes_available < self.capacity/4:
            return True
        else:
            return False
        return self.bikes_available < self.capacity/4
    def __str__(self):
        return f"{'Grand Army Plaza : 6 of 48 bikes'}, {self.name}:{self.bikes_available} of {self.capacity} bikes"

    
# TODO: add __str__(self) to return text like "Grand Army Plaza: 6 of 48 bikes" done
# TODO: build it from self.name, self.bikes_available and self.capacity
# TODO: rebuild `fleet` from this class with the same loop as Step 2

print(fleet[0])
print(fleet[:2])

# Step 3, answer 1:
#
# Step 3, answer 2:
#


# Step 4: Add `__repr__` and Print the Van List for You and the Dispatcher
# TODO: copy your Station class from Step 3 here
# TODO: add __repr__(self) to return text like "Station('Grand Army Plaza', 6)"
# TODO: rebuild `fleet` from this class with the same loop as Step 2
# TODO: assign `van_list` to []; loop over `fleet`
# TODO: append each station whose needs_restock() returns True to `van_list`

print(van_list)
for station in van_list:
    print(station)

# Step 4, answer 1:
#
# Step 4, answer 2:
#
# Step 4, answer 3:
#
