# Utility module used to implement functions for opening/loading data from CSV files and accessing respective data
import csv
import main

# Method used to open CSV file, extract address distance data, and insert into a 2-D list named distanceInfoList
distanceInfoList = []  # List for holding the address distance information
def loadDistances(fileNm):
    with open(fileNm, encoding='utf-8-sig') as distancesFile:
        distanceInfo = csv.reader(distancesFile)

        # Place all values into the list
        for val in distanceInfo:
            distanceInfoList.append(val)


# Method used to open CSV file, extract address ID/street data, and insert into a 2-D list named addressInfoList
addressInfoList = []  # List for holding addresses and their corresponding ID's
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

# FIXME Method used to obtain the closest address ID, given a list of package IDs, from the input address
def dispatchNearestPackages(truck):
    # From the truck's package ID list, pull package objects from hash table and append into a list
    pkgList = []
    for pkgID in truck.loaded_packages:
        pkgObj = main.pckgHashTbl.tblLookUp(pkgID)
        pkgList.append(pkgObj)

    truck.loaded_packages.clear()  # FIXME-->MAY NOT NEED, TEST WITHOUT

    lowest_mileage_val = None  # Assign an arbitrary value larger than any mileage between two addresses
    currentAddyID = getAddyId(truck.current_address)  # Obtain current address's ID and assign to variable

    # This will run while there are still packages on the truck to be delivered
    while len(pkgList) > 0:


        # This will find the address nearest to the current address
        for pkg in pkgList:  # Loop through list of package IDs
            # pkgObj = main.pckgHashTbl.tblLookUp(pkgID)  # Find package object in hash table and assign to variable
            addyID = getAddyId(pkg.d_address)  # Obtain the package object's address ID
            miles = distanceBtwn(currentAddyID, addyID)  # Find the distance between current address and the package's address
            print("Package #" + str(pkg.package_id) + ", Distance: " + str(miles))  # FIXME-->Remove later

            # If the current package's address is closer than the lowest mileage value thus far, assign the current
            # package's mileage value as the lowest value and set the current package's ID as the nearest ID
            if lowest_mileage_val is None or miles <= lowest_mileage_val:
                lowest_mileage_val = miles
                nearestAddyID = addyID
                print("lowest distance: " + str(lowest_mileage_val))  # FIXME-->Remove later

                currentAddyID = nearestAddyID  # Nearest address TODO
                pkgList.remove(pkg)

            truck.mileage += lowest_mileage_val
            # TODO update truck current time with--> truck.current_time += datetime.timedelta(hours=lowest_mileage_val / 18)
            # TODO pkg.deliver_time = truck.current_time
            pkg.d_status = "Delivered"  # FIXME-->MAY NOT NEED




# FIXME!!!!! DELETE?
def dispatchPackages(truck):
    while len(truck.loaded_packages) > 0:
        currentAddy = truck.current_address
        # nextAddy = nearestAddress(currentAddy, truck.loaded_packages)
