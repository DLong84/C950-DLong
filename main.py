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
# to variables. Assigning to variables is necessary for being able to access/manipulate each truck's data.
#
# Packages are assigned and grouped to certain trucks based on their delays, delivery deadlines, and address vicinities.

# Truck 1's early departure time of 8:00am is based off of most of its packages having early delivery deadlines.
truck1 = Truck(1, "4001 South 700 East", datetime.timedelta,
               datetime.timedelta(hours=8, minutes=0), [1,4,7,8,13,14,15,16,20,21,29,30,31,34,37,40],
               0.0)

# Trucks 2's departure time is calculated based off of trucks 1 & 3 returning to the hub. If their return times are
# earlier than 10:20am, then truck 2's departure time will be 10:20am to account for an erroneous address being updated
# at 10:20am. If they return later than 10:20am, then truck 2's departure time will be the earlier of the two. Its
# packages have EOD delivery deadlines, so the later departure will not be an issue.
truck2 = Truck(2, "4001 South 700 East", None,
               None, [2,3,5,9,10,11,12,18,23,24,27,33,35,36,38,39],0.0)

# Truck 3's departure time of 9:05am is to account for some its packages not arriving at the hub until that time.
truck3 = Truck(3, "4001 South 700 East", datetime.timedelta,
               datetime.timedelta(hours=9, minutes=5), [6,17,19,22,25,26,28,32],0.0)

# ---------------------------------------------------------------------------------------------------------------------
# Start of UI
# -----------------
# Print the title
print("*" * 100)
print("                             Western Governors University Parcel Service                             ")
print("*" * 100 + '\n')

# Print truck mileage
print(f"------- Total mileage for all trucks is: {truck1.mileage + truck2.mileage + truck3.mileage} -------")
