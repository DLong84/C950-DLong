# This class represents a package object for storing package information data
import csv
import hash_tbl

class Package:
    # The Package object constructor....FIXME--->keep an eye on deliver_time during instantiation!!
    def __init__(self, package_id, d_address, d_deadline, d_city, d_state, d_zipcode, weight, d_status, depart_time,
                 deliver_time):
        self.package_id = package_id
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

    # Method used to open CSV file, extract package data, and insert into hash table
    # Source: W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py
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
                d_status = "At hub"
                depart_time = None
                deliver_time = None

                # Instantiate the package object
                package = Package(package_id, d_address, d_deadline, d_city, d_state, d_zipcode, weight,
                                  d_status, depart_time, deliver_time)

                # Insert package into hash table
                my_table.add_to_table(package_id, package)  # package_id is used as key

    # FIXME-->Method used to update a Package object's status
    # TODO-->TEST THIS
    def update_status(self, time_probed):
        if time_probed <= self.deliver_time:
            self.d_status = "At hub"
        elif self.depart_time <= time_probed < self.deliver_time:
            self.d_status = "En route"
        elif time_probed >= self.deliver_time:
            self.d_status = f"Delivered at: {self.deliver_time}"
        # TODO-->Watch for showing/hiding delivery time depending on time
