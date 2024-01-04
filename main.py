# Author...Name: David Long, Student ID: 006813910

from package import Package
from hash_tbl import HashTable

# FIXME---> TEST DATA:

testPackage1 = Package(1, "Ritz-Carlton Hotel", "9pm", "Chattanooga",
                      "TN", "37343","12","?")
testPackage2 = Package(2, "222 Apian Way", "EOD", "Apison",
                      "TN", "37309","15","?")
testPackage3 = Package(3, "555 Hunter Rd", "9pm", "Harrison",
                      "TN", "37341","1","?")
testPackage4 = Package(41, "345 Bank Circle", "9pm", "Ooltewah",
                      "TN", "37363","10","?")

sample_table = HashTable()

HashTable.add_to_table(sample_table, testPackage1.package_id, testPackage1)
HashTable.add_to_table(sample_table, testPackage2.package_id, testPackage2)
HashTable.add_to_table(sample_table, testPackage3.package_id, testPackage3)

print("Table elements: " + str(sample_table.elements))

# print(str(testPackage))
# print("Search function returned:")
# print(sample_table.tblLookUp(-1))


Package.loadPackageInfo("CSV/packages.csv", sample_table)  # LOAD Package data into hah table

HashTable.add_to_table(sample_table, testPackage4.package_id, testPackage4)

HashTable.printAllPkgs(sample_table)

print("Table elements: " + str(sample_table.elements))

pckg1 = sample_table.tblLookUp(41)  # -->***Pull object from table into variable
print(pckg1.d_deadline)
pckg1.d_deadline = "9:30pm"
print(pckg1)