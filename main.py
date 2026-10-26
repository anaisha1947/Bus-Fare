# Make a child class for the Bus that inherits from the Vehicle class. 
# Any vehicle's default fare price is seating capacity * 100. 
# For example, we must add a maintenance charge of 10% to the full fare. 
# As a result, the final fare for a bus ride will be equal to the total fare
# plus 10% of the total fare.
# The bus has a seating capacity of 50 people. 
# As a result, the total fare should be INR 5500. 
# In the Bus class, you must override the fare() method of the Vehicle class.

class Vehicle:
    def __init__(self, seats, fare_price=100):
        self.seats = seats
        self.fare_price = fare_price
    def fare(self):
        return self.seats * self.fare_price      
    def display(self):
        print(f"Seating Capacity: {self.seats}")
        print(f"Fare Price: {self.fare_price}")
        print(f"Final Price: {self.fare()}")
class Bus(Vehicle):
    def __init__(self, seats=50):
        super().__init__(seats)  
    def fare(self):
        total_fare = super().fare()
        final_fare = total_fare * 1.1
        return int(final_fare)
bus = Bus()
bus.display()
