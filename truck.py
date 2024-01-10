# This class represents a truck object for storing truck information data
class Truck:
    # The Truck object constructor
    def __init__(self, truck_id, current_address, current_time, departure_t, loaded_packages, mileage):
        self. truck_id = truck_id
        self.current_address = current_address
        self.current_time = departure_t
        self.departure_t = departure_t
        self.loaded_packages = loaded_packages  # FIXME-->Keep an eye on this!
        self.mileage = mileage

        # String method to define how package objects should be shown as a string
        def __str__(self):  # TODO ????
            pass