# Utility module used to implement functions for opening/loading data from CSV files and accessing respective data

import csv
import datetime
from package import Package

# Method used to open CSV file, extract package data, and insert into hash table. Every row in the file corresponds
# to a different package object.
# Source: W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py
def loadPackageInfo(fileNm, my_table):
    with open(fileNm) as deliveryPackages:
        packageInfo = csv.reader(deliveryPackages, delimiter=',')
        next(packageInfo)
        # Go down the file, row by row, and load the row's data into the package's attributes
        for pkg in packageInfo:
            package_id = int(pkg[0])
            trk_id = None
            d_address = pkg[1]
            d_city = pkg[2]
            d_state = pkg[3]
            d_zipcode = pkg[4]
            d_deadline = pkg[5]
            weight = pkg[6]
            d_status = None
            depart_time = None
            deliver_time = None

            # Instantiate the package object
            package = Package(package_id, trk_id, d_address, d_deadline, d_city, d_state, d_zipcode, weight,
                              d_status, depart_time, deliver_time)

            # Insert package into hash table
            my_table.add_to_table(package_id, package)  # package_id is used as key

# Method used to open CSV file, extract address ID/street data, and insert into a 2-D list named addressInfoList
addressInfoList = []  # Global list for holding addresses and their corresponding ID's
def loadAddresses(fileNm):
    with open(fileNm, encoding='utf-8-sig') as addressesFile:
        addressInfo = csv.reader(addressesFile)

        # Place only the ID and street address into the list
        for val in addressInfo:
            addressInfoList.append([val[0], val[2]])

# Method used to obtain the ID of an address
def getAddyId(address):
    for row in addressInfoList:
        # If the addresses match, return the ID number
        if row[1] == address:
            return int(row[0])

# Method used to obtain the name of an address from its corresponding ID
def getAddyName(address):
    for row in addressInfoList:
        # If the addresses match, return the name
        if row[0] == str(address):
            return row[1]

# Function used to open CSV file, extract address distance data, and insert into a 2-D list named distanceInfoList
distanceInfoList = []  # Global list for holding the address distance information
def loadDistances(fileNm):
    with open(fileNm, encoding='utf-8-sig') as distancesFile:
        distanceInfo = csv.reader(distancesFile)

        # Place all values into the list
        for val in distanceInfo:
            distanceInfoList.append(val)

# Method used to obtain the float mileage value between two addresses. Input addresses can be either strings or integers
def distanceBtwn(add1, add2):
    if isinstance(add1, str) and isinstance(add2, str):  # If addresses are strings
        # Obtain and assign respective ID's to the addresses
        add1 = getAddyId(add1)
        add2 = getAddyId(add2)

    if distanceInfoList[add1][add2] == '':  # Flip addresses if there is no value in the list index
        return float(distanceInfoList[add2][add1])
    else:
        return float(distanceInfoList[add1][add2])

# This function is the main algorithm for delivering packages and updating truck attributes, including mileage,
# offloading packages, and tracking/updating times. It utilizes the "nearest neighbor" algorithm by selecting the
# closest package to the truck's current address, moving the truck to that location, and removing the delivered package
# until no packages remain for delivery. It returns trucks 1 and 3 back to the starting hub when finished.
def dispatchNearestPackages(truck, my_table):  # Hash table parameter creates dependency injection for flexibility

    # From the truck's list of package IDs, pull package objects from hash table, add the corresponding truck's ID,
    # and append into a list
    pkgList = []  # Initialize an empty list for holding package objects
    for pkgID in truck.loaded_packages:  # For every package ID in the truck's loaded_packages list:
        pkgObj = my_table.tblLookUp(pkgID)  # Find/pull package from hash table using the lookup method and assign to variable
        pkgObj.trk_id = truck.truck_id  # Connect package to truck by setting the package's truck ID to the truck's ID
        pkgObj.depart_time = truck.departure_t  # Set the package's departure time to the truck's departure time
        pkgList.append(pkgObj)  # Add the package object to list

    truck.loaded_packages.clear()  # Clear the truck's list of package IDs. This is done for scalability, such as adding
                                   # new features for loading the truck with new packages for subsequent deliveries.

    currentAddyID = getAddyId(truck.current_address)  # Obtain the truck's starting address's ID and assign to variable.
                                                      # This variable will be used to keep track of the truck's current
                                                      # address as it moves to delivery addresses.

    # This will run while there are still packages on the truck to be delivered
    while len(pkgList) > 0:
        lowest_mileage_val = None  # Initialize a variable for holding the lowest mileage value and assign an arbitrary
                                   # starting value. This variable's value will be used for comparison to the mileage
                                   # value of each package in order to find the closest package.

        # This block is based off of the "nearest neighbor" algorithm. It will calculate the distance from the truck's
        # current address to each package's delivery address. It will then compare all the packages' distance values and
        # select the package with the lowest distance (nearest neighbor) for delivery.
        for pkg in pkgList:  # For every package in the truck's current list of package objects:

            addyID = getAddyId(pkg.d_address)  # Obtain the package object's address ID and assign to a variable
            miles = distanceBtwn(currentAddyID, addyID)  # Get distance between current address and package's address
                                                         # and assign that value to a variable.

            # If the current package's address is closer than the lowest mileage value thus far, assign the current
            # package's mileage value as the lowest value and set the current package's ID as the nearest ID
            #
            if lowest_mileage_val is None or miles <= lowest_mileage_val:  # If this is the first package in the list or
                                    # the package's distance is less than or equal to the current lowest mileage value:

                lowest_mileage_val = miles  # Assign the package's distance value as the lowest distance value

                nearestAddyID = addyID  # Assign the package's address ID to the variable for holding the closest
                                        # address's ID

                pkgToDeliver = pkg  # Assign the package object to a variable for holding the nearest package

        # When the previous block is done comparing all package distances, this block updates the truck's and closest
        # package's attributes utilizing the last known values of the lowest distance value and closest address ID.
        currentAddyID = nearestAddyID  # Update the current address's ID to the closest package's address ID

        truck.current_address = getAddyName(currentAddyID)  # Update the truck's current address to the closest package's
                                                            # address (Move the truck to the next delivery address)

        truck.mileage += lowest_mileage_val  # Add the lowest distance value (distance to the closest package) to the
                                             # truck's accumulated mileage value

        truck.current_time += datetime.timedelta(hours=lowest_mileage_val / 18)  # Calculate the travel time to the
            # closest address (divide the distance by the truck's average speed (18mph)) and add that value to the
            # truck's accumulated current time value

        pkgToDeliver.deliver_time = truck.current_time  # Assign the truck's updated current time value to the closest
                                                        # package's delivery time

        pkgList.remove(pkgToDeliver)  # Remove the nearest package from the truck's list of packages. The package has
                                      # been updated with everything and is not needed for further calculations

                    # The "while" block now restarts with the remaining packages in the truck's list ->

    # This block executes when the list of packages for trucks 1 and truck 3 is empty
    # Return trucks 1 and 3 to hub
    if truck.truck_id in [1, 3]:  # If the truck's ID is 1 or 3:

        miles = distanceBtwn(currentAddyID, 0)  # Get the distance between the truck's current address and the hub.
                                                     # '0' is the hub's known address ID

        truck.mileage += miles  # Add the distance to the hub to the truck's accumulated mileage value

        truck.current_time += datetime.timedelta(hours=miles / 18)  # Calculate the travel time to the hub (divide the
                        # distance by the truck's average speed (18mph)) and add that value to the truck's accumulated
                        # current time value

        truck.current_address = getAddyName(0)  # Update truck's current address to the hub's address. '0' is the hub's
                                                # known address ID