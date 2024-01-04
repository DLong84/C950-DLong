# This class represents a package object for storing package information data
import csv
import hash_tbl

class Package:
    # The Package object constructor....FIXME--->keep an eye on d_time during instantiation!!
    def __init__(self, package_id, d_address, d_deadline, d_city, d_state, d_zipcode, weight, d_status, d_time="pending"):
        self.package_id = package_id
        self.d_address = d_address
        self.d_deadline = d_deadline
        self.d_city = d_city
        self.d_state = d_state
        self.d_zipcode = d_zipcode
        self.weight = weight
        self.d_status = d_status
        self.d_time = d_time

    # String method to define how package objects should be shown as a string
    def __str__(self):
        return (f"PackageID: {self.package_id}, Address: {self.d_address}, City: {self.d_city}, State: {self.d_state}, "
                f"Zip: {self.d_zipcode}, Deadline: {self.d_deadline}, Weight (KILO): {self.weight}, Status: {self.d_status}, "
                f"Delivery Time: {self.d_time}")

    # Method to open CSV file, extract package data, and insert into hash table
    def loadPackageInfo(fileNm, my_table):
        with open(fileNm) as deliveryPackages:
            packageInfo = csv.reader(deliveryPackages, delimiter=',')
            next(packageInfo)
            for pkg in packageInfo:
                package_id = int(pkg[0])
                d_address = pkg[1]
                d_city = pkg[2]
                d_state = pkg[3]
                d_zipcode = pkg[4]
                d_deadline = pkg[5]
                weight = pkg[6]
                delivery_status = "At hub"
                d_time = "pending"

                # Instantiate the package object
                package = Package(package_id, d_address, d_deadline, d_city, d_state, d_zipcode, weight, delivery_status, d_time)
                # print(package)

                # TODO-->Hash table insert function goes here
                my_table.add_to_table(package_id, package)  # package_id is used as key










    # FIXME-->Method used to retrieve a Package object's status
    def get_status(self, package_id):
        # TODO implement how to pull package status

        return None
