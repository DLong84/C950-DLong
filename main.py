# Author...Name: David Long, Student ID: 006813910

from package import Package
from hash_tbl import HashTable

# FIXME---> TEST DATA:

testPackage = Package(2, "Ritz-Carlton Hotel", "9pm", "Chattanooga",
                      "37341","12","?")
sample_table = HashTable()
print("Table elements: " + str(sample_table.elements))
HashTable.add_to_table(sample_table, testPackage.package_id, testPackage)
print("Table elements: " + str(sample_table.elements))
print(str(testPackage))

print()  # FIXME-->Need to implement and test search function