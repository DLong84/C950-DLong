# This class represents a truck object for storing truck information data
class Truck:
    # The Truck object constructor
    def __init__(self, truck_id, current_address, current_time, departure_t, loaded_packages, mileage):
        self. truck_id = truck_id
        self.current_address = current_address
        self.current_time = departure_t  # The truck's current time will be initialized to the hub departure time
        self.departure_t = departure_t  # Truck's time of departure from the hub
        self.loaded_packages = loaded_packages  # The list of packages assigned to the truck
        self.mileage = mileage  # Will be used for keeping track of a truck's mileage accrued for deliveries