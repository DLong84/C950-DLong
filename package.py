# This class represents a package object for storing package information data
import csv
import datetime

import hash_tbl

class Package:
    # The Package object constructor
    def __init__(self, package_id, trk_id, d_address, d_deadline, d_city, d_state, d_zipcode, weight, d_status,
                 depart_time, deliver_time):
        self.package_id = package_id
        self.trk_id = trk_id
        self.d_address = d_address
        self.d_deadline = d_deadline
        self.d_city = d_city
        self.d_state = d_state
        self.d_zipcode = d_zipcode
        self.weight = weight
        self.d_status = d_status
        self.depart_time = depart_time
        self.deliver_time = deliver_time

    # String method to define how package objects should be shown as a string
    def __str__(self):
        return (f"PackageID: {self.package_id}, Address: {self.d_address}, City: {self.d_city}, State: {self.d_state}, "
                f"Zip: {self.d_zipcode}, Deadline: {self.d_deadline}, Weight (KILO): {self.weight}, "
                f"Status: {self.d_status}")

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

    # Method used to update a Package object's status and text color depending on the time. ANSI escape codes are
    # utilized for the output status text color changes.
    # Source: https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python
    def update_status(self, time_probed):
        # Update package's delivery status, depending on the time
        if self.depart_time is None or time_probed < self.depart_time:
            self.d_status = "\033[91mAt hub \033[0m"  # Red text
        elif self.depart_time <= time_probed < self.deliver_time:
            self.d_status = f"\033[93mEn route on Truck-{self.trk_id}\033[0m"  # Yellow text
        elif time_probed >= self.deliver_time:
            self.d_status = f"\033[92mDelivered by Truck-{self.trk_id} at {self.deliver_time}\033[0m"  # Green text

        # Update package #9's address, depending on the time
        if self.package_id == 9 and time_probed < datetime.timedelta(hours=10, minutes=20):
            self.d_address = "300 State St"
            self.d_zipcode = "84103"
        elif self.package_id == 9 and time_probed >= datetime.timedelta(hours=10, minutes=20):
            self.d_address = "410 S State St"
            self.d_zipcode = "84111"
