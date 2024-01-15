# Class used to implement methods for building a self-adjusting hash table of package objects

class HashTable:
    # Hash table constructor
    # Hash table has a load factor of <=1 to eliminate collisions
    def __init__(self, starting_size=40):
        self.size = starting_size
        self.elements = 0
        self.table = [None] * starting_size # Create the table structure

    # This method is implemented to allow for iterating through the hash table. Iteration is used in
    # dispatchNearestPackages() for creating a list of package objects from the hash table.
    def __iter__(self):
        return iter(self.table)

    # Method used to insert package objects into hash table buckets and check the load factor for self-adjustment
    def add_to_table(self, key, pkg):
        # Check load factor & resize if table is full
        load = self.elements / self.size  # The load = (Packages currently in the table)/(the table's current size)
        if load >= 1:  # If the table is full
            self.resize()  # Call the resize method to resize the hash table

        bckt = hash(key) % self.size  # Calculate bucket from hash
        if self.table[bckt] is None:  # If bucket is empty
            self.table[bckt] = pkg  # Place the package in the bucket
            self.elements += 1  # Add 1 to the number of elements currently in the table

        # print("Package with ID: " + str(pkg.package_id) + ", successfully added to hash table")
        # print(self.table)

    # Method used to adjust the size of the hash table to keep a 1-1 mapping and prevent collisions. This is what keeps
    # the hash table as a self-adjusting data structure.
    def resize(self):
        newTableSize = self.size * 2  # Double the table size
        resizedTable = [None] * newTableSize  # Rebuild the table structure to reflect the new size

        # Rehash and insert existing package objects into new hash table
        for pkg in self.table:  # Go through hash table
            if pkg is not None:  # As long as a package exists in the bucket
                key = pkg.package_id  # Pull package id and assign as key
                newBkt = hash(key) % newTableSize  # Calculate the new bucket from updated hash function
                resizedTable[newBkt] = pkg  # Place the package in the new bucket

        # Assign initial table variables with the new table values
        self.table = resizedTable
        self.size = newTableSize

        # print("Hash table size has been adjusted to " + str(self.size))

    # Method used to retrieve package object data from the hash table
    def tblLookUp(self, pkg_id):
        # Calculate the package's bucket in the hash table using the package ID (key)
        bucket = hash(int(pkg_id)) % self.size
        # If the package does not exist or the ID is outside the scope of the hash table (being too big or too small)
        if self.table[bucket] is None or int(pkg_id) > self.size or int(pkg_id) < 1:
            print("Package ID not found, please try again")
            return False
        # Otherwise, return the package object containing its attributes/data
        else:
            return self.table[bucket]

    # Method used to display all existing hash table package objects and their data (in numerical order)
    def printAllPkgs(self):
        for pkg in self.table[1:]:  # All package except the first
            if pkg is not None:  # If package object exists
                print(pkg)
        print(self.table[0])  # Display the first package at the end (package 40)