# This class represents a truck object for storing truck information data
class Truck:
    # The Truck object constructor
    def __init__(self, truck_id, loaded_packages, mileage=0):
        self. truck_id = truck_id
        self.loaded_packages = loaded_packages  # FIXME-->Keep an eye on this!
        self.mileage = mileage
