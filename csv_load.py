# Class used to implement methods for opening/loading data from CSV files and accessing respective data
import csv


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

# Method used to obtain the float mileage value between two addresses
def distanceBtwn(add1, add2):
    # Obtain and assign respective ID's to the addresses
    add1 = getAddyId(add1)
    add2 = getAddyId(add2)

    if distanceInfoList[add1][add2] == '':  # Flip addresses if there is no value in the list index
        return float(distanceInfoList[add2][add1])
    else:
        return float(distanceInfoList[add1][add2])