# Utility module used to implement functions for opening/loading data from CSV files and accessing respective data
import csv
import datetime

import main


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
def getAddyName(address):  # FIXME-->May not be needed
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

# FIXME Function used to obtain the closest address ID, given a list of package IDs, from the input address
def dispatchNearestPackages(truck):
    # From the truck's list of package IDs, pull package objects from hash table, add the corresponding truck's ID,
    # and append into a list
    pkgList = []
    for pkgID in truck.loaded_packages:
        pkgObj = main.pckgHashTbl.tblLookUp(pkgID)  # Find/pull package from hash table and assign to variable
        pkgObj.trk_id = truck.truck_id  # Assign the package to the truck
        pkgObj.depart_time = truck.departure_t  # TODO-->Keep an eye on this for truck 2's departure!!
        pkgList.append(pkgObj)  # Add package object to list

    truck.loaded_packages.clear()  # FIXME-->MAY NOT NEED, TEST WITHOUT


    currentAddyID = getAddyId(truck.current_address)  # Obtain truck's current address's ID and assign to variable

    # This will run while there are still packages on the truck to be delivered
    while len(pkgList) > 0:
        lowest_mileage_val = None  # Assign an arbitrary starting value

        # This will TODO
        for pkg in pkgList:  # Loop through list of package IDs

            addyID = getAddyId(pkg.d_address)  # Obtain the package object's address ID
            miles = distanceBtwn(currentAddyID, addyID)  # Get distance between current address and package's address
            print("Package #" + str(pkg.package_id) + ", Distance: " + str(miles))  # FIXME-->Remove later

            # If the current package's address is closer than the lowest mileage value thus far, assign the current
            # package's mileage value as the lowest value and set the current package's ID as the nearest ID
            if lowest_mileage_val is None or miles <= lowest_mileage_val:
                lowest_mileage_val = miles
                nearestAddyID = addyID
                pkgToDeliver = pkg
                print("lowest distance: " + str(lowest_mileage_val))  # FIXME-->Remove later

        currentAddyID = nearestAddyID  # Nearest address TODO
        truck.current_address = getAddyName(currentAddyID)  # Update truck's address name
        print(f"Truck's current addy: {truck.current_address}")
        truck.mileage += lowest_mileage_val
        truck.current_time += datetime.timedelta(hours=lowest_mileage_val / 18)
        pkgToDeliver.deliver_time = truck.current_time
        pkgList.remove(pkgToDeliver)  # FIXME-->Unload the package using pkg ID?
        print(pkgList)
        print(f"Truck total miles: {truck.mileage}")

    # Return truck to hub
    if truck.truck_id == 1:  # TODO-->May need to use truck 3 instead, depending on which gets done earlier
        miles = distanceBtwn(currentAddyID, 0)  # Distance from current address back to hub
        truck.mileage += miles
        truck.current_time += datetime.timedelta(hours=miles / 18)
        truck.current_address = getAddyName(0)  # Update truck's address name
        print(main.truck1.current_time)
        main.truck2.departure_t = truck.current_time  # FIXME-->Need to account for package 9's address change at 10:20am!!
        main.truck2.current_time = main.truck2.departure_t


