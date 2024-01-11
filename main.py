# Author: David Long
# Student ID: 006813910
# WGU C950 Project

import datetime
import utilities
from package import Package
from hash_tbl import HashTable
from truck import Truck

# Load distance data from files
utilities.loadDistances("CSV/address_distances.csv")

# Load address data from files
utilities.loadAddresses("CSV/delivery_addresses.csv")

# Instantiate hash table object and assign to variable. Assigning to a variable is necessary for being able to access
# the hash table and its contents
pckgHashTbl = HashTable()
Package.loadPackageInfo("CSV/packages.csv", pckgHashTbl)  # Load package data from file into hash table

# Instantiate the 3 truck objects, along with their attributes including their packages to be delivered and assign
# to variables. Assigning to variables is necessary for being able to access/manipulate each truck's data
truck1 = Truck(1, "4001 South 700 East", datetime.timedelta,
               datetime.timedelta(hours=8, minutes=0), [1,13,14,15,16,20,29,30,31,34,37,40],0.0)

truck2 = Truck(2, "4001 South 700 East", None,
               None, [3,9,18,36,38],0.0)

truck3 = Truck(3, "4001 South 700 East", datetime.timedelta,
               datetime.timedelta(hours=9, minutes=5), [6,25,28,32],0.0)

# ---------------------------------------------------------------------------------------------------------------------
# Start of UI
# -----------------
# Print the title
print("*" * 100)
print("                             Western Governors University Parcel Service                             ")
print("*" * 100 + '\n')

# Print truck mileage
print(f"------- Total mileage for all trucks is: {truck1.mileage + truck2.mileage + truck3.mileage} -------")
