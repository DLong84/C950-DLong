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
utilities.loadPackageInfo("CSV/packages.csv", pckgHashTbl)  # Load package data from file into hash table

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

# Deliver packages on trucks 1 & 3
utilities.dispatchNearestPackages(truck1, pckgHashTbl)
utilities.dispatchNearestPackages(truck3, pckgHashTbl)

# If trucks 1 & 3 return to the hub before package #9's correct address is given, set truck 2's current and departure
# times to 10:20am, otherwise set truck 2's current and departure times to the time the first truck arrives back to the
# hub.
if truck1.current_time and truck3.current_time < datetime.timedelta(hours=10, minutes=20):
    truck2.departure_t = datetime.timedelta(hours=10, minutes=20)
    truck2.current_time = truck2.departure_t
else:
    truck2.departure_t = min(truck1.current_time, truck3.current_time)
    truck2.current_time = truck2.departure_t

# Deliver packages on truck 2
utilities.dispatchNearestPackages(truck2, pckgHashTbl)


# ---------------------------------------------------------------------------------------------------------------------
# Start of UI
# -----------------
# Print the title
print("*" * 100)
print("                             Western Governors University Parcel Service                             ")
print("*" * 100 + '\n')

# Print truck mileage
print(f"------- Total mileage for all trucks is: {truck1.mileage + truck2.mileage + truck3.mileage} miles -------")
print("-" * 100 + '\n')

while True:
    # Obtain user input option for what they want to view and assign as a variable. The program continues until "Q" is
    # user's input.
    user_reqst = input(f"Hello, please pick an option below and press enter: \n"
                             f"(1) ->View a single package status at a certain time\n"
                             f"(2) ->View all packages' status at a certain time\n"
                             f"(Q) ->Exit the program\n >>>").lower()

    # User decides to exit the program by choosing "Q":
    if user_reqst == "q":
        print("Goodbye")
        break

    # User decides to view a package's status at a certain time by choosing "1"
    if user_reqst == "1":
        # Get the requested package ID, cast to an int and obtain the package object from the hash table. Assign the
        # package object as a variable.
        pkg_id = int(input("Please enter a package ID number: "))
        pkg = None
        while pkg is None or pkg is False:  # While user input is not found
            pkg = pckgHashTbl.tblLookUp(pkg_id)  # Look for package in hash table
            if pkg is not None and pkg is not False:  # When the package is found, break out of the loop and continue on
                continue
            pkg_id = int(input("Please enter a valid package ID number: "))  # This is skipped if the package is found

        # Get the requested time, split the string into ints and assign them as proper variables. Place the variables
        # into the timedelta and reassign as the variable value.
        while True:  # Loop will run as long as the time is input incorrectly, raising a ValueError
            try:
                inputTime = input("Please enter a time in military (HH:mm) format: ")
                hrs, mins = map(int, inputTime.split(':'))
                inputTime = datetime.timedelta(hours=hrs, minutes=mins)
                break  # When the time is input correctly, break out of the loop and continue on
            except ValueError:
                print("Improper time format, please try again")

        # Update the status of the package for the input time and print it to the user
        pkg.update_status(inputTime)
        print("\n")
        print(pkg)
        print("\n")

    # User decides to view all packages' status at a certain time by choosing "2"
    if user_reqst == "2":
        # Get the requested time, split the string into ints and assign them as proper variables. Place the variables
        # into the timedelta and reassign as the variable value.
        while True:  # Loop will run as long as the time is input incorrectly, raising a ValueError
            try:
                inputTime = input("Please enter a time in military (HH:mm) format: ")
                hrs, mins = map(int, inputTime.split(':'))
                inputTime = datetime.timedelta(hours=hrs, minutes=mins)
                break  # When the time is input correctly, break out of the loop and continue on
            except ValueError:
                print("Improper time format, please try again")

        # Update the status of all packages for the input time and print them to the user
        for pkg in pckgHashTbl:
            if pkg is not None:
                pkg.update_status(inputTime)


        pckgHashTbl.printAllPkgs()
        print("\n")
