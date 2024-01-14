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
        load = self.elements / self.size
        if load >= 1:
            self.resize()

        bckt = hash(key) % self.size  # Calculate bucket from hash
        if self.table[bckt] is None:
            self.table[bckt] = pkg  # Add pkg to bucket
            self.elements += 1

        # print("Package with ID: " + str(pkg.package_id) + ", successfully added to hash table")
        # print(self.table)

    # Method used to adjust the size of the hash table to keep a 1-1 mapping and prevent collisions
    def resize(self):
        newTableSize = self.size * 2  # Double the table
        resizedTable = [None] * newTableSize  # Rebuild the table structure to reflect the new size

        # Rehash and insert existing package objects into new hash table
        for pkg in self.table:
            if pkg is not None:
                key = pkg.package_id  # Pull package id
                newBkt = hash(key) % newTableSize  # Calculate bucket from updated hash function
                resizedTable[newBkt] = pkg  # Add pkg to bucket

        # Assign initial table variables with new table values
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