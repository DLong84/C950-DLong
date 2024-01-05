# Class used to implement methods for opening and loading data from CSV files
import csv


# Method used to open CSV file, extract address distance data, and insert into a 2-D list
def loadDistances(fileNm):
    with open(fileNm, encoding='utf-8-sig') as distancesFile:
        distanceInfoList = csv.reader(distancesFile)
        distanceInfoList = list(distanceInfoList)
        return distanceInfoList

# Method used to open CSV file, extract address ID/street data, and insert into a 2-D list
def loadAddresses(fileNm):
    addressInfoList = []
    with open(fileNm, encoding='utf-8-sig') as addressesFile:
        addressInfo = csv.reader(addressesFile)

        # Place only the ID and street address into the list
        for val in addressInfo:
            addressInfoList.append([val[0], val[2]])
        return addressInfoList
