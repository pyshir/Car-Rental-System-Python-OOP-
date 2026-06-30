# Car Rental System
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name, rent_per_day, available):
        self.name = name
        self.rent_per_day = rent_per_day
        self.__available = available

    def get_available(self):
        return self.__available
    
    def set_available(self, available):
        self.__available = available

    
    def rent(self):
        if self.__available:
            self.__available = False
            print('Successfully rented')
        else:
            print('Sorry not available to rent')

    
    def return_vehicle(self):
        if not self.__available:
            self.__available = True
            print('Returned Successfully')
        else:
            print('Not rented at all')

    @abstractmethod
    def calculate_bill(self):
        pass


class Car(Vehicle):
    def __init__(self, name, rent_per_day, available):
        super().__init__(name, rent_per_day, available)
        

    def calculate_bill(self, days):
        total_bill = self.rent_per_day * days
        discount_bill = int(total_bill * 0.95)
        print(f'Your total bill is, {discount_bill}') 

class Bike(Vehicle):
    def __init__(self, name, rent_per_day, available):
        super().__init__(name, rent_per_day, available)

    def calculate_bill(self, days):
        total_bill = self.rent_per_day * days
        discount_bill = total_bill
        print(f'Your total bill is, {discount_bill}') 

class Bus(Vehicle):
    def __init__(self, name, rent_per_day, available):
        super().__init__(name, rent_per_day, available)

    def calculate_bill(self, days):
        total_bill = self.rent_per_day * days
        discount_bill = int(total_bill * 0.90)
        print(f'Your total bill is, {discount_bill}') 

class Vehicles:
    def __init__(self):
        self.vehicles = [car, bike, bus]

    def show_vehicles(self):
        for vehicle in self.vehicles:
            if isinstance(vehicle, Car):
                print(f'Type: Car, Brand: {vehicle.name}, Rent: {vehicle.rent_per_day}/Day, Available: {vehicle.get_available()}')
            if isinstance(vehicle, Bike):
                print(f'Type: Bike, Brand: {vehicle.name}, Rent: {vehicle.rent_per_day}/Day, Available: {vehicle.get_available()}')
            if isinstance(vehicle, Bus):
                print(f'Type: Bus, Brand: {vehicle.name}, Rent: {vehicle.rent_per_day}/Day, Available: {vehicle.get_available()}')

    def rent_vehicle(self):
        print("""
1.Car
2.Bike
3.Bus
              """)
        
        vehicle_type = input('Choose vehicle type:\n=')

        if vehicle_type == '1':
            car.rent()
        if vehicle_type == '2':
            bike.rent()
        if vehicle_type == '3':
            bus.rent()

    def return_vehicles(self):
        print("""
1.Car
2.Bike
3.Bus
              """)
        
        vehicle_type = input('Choose vehicle type:\n=')

        if vehicle_type == '1':
            car.return_vehicle()
        if vehicle_type == '2':
            bike.return_vehicle()
        if vehicle_type == '3':
            bus.return_vehicle()

    def bill(self):
        print("""
1.Car
2.Bike
3.Bus
              """)
        
        vehicle_type = input('Choose vehicle type:\n=')

        if vehicle_type == '1':
            vehicle = self.vehicles[0]
            days = int(input('how many days rent for\n='))
            vehicle.calculate_bill(days)
        if vehicle_type == '2':
            vehicle = self.vehicles[1]
            days = int(input('how many days rent for\n='))
            vehicle.calculate_bill(days)
        if vehicle_type == '3':
            vehicle = self.vehicles[2]
            days = int(input('how many days rent for\n='))
            vehicle.calculate_bill(days)

        
    
   



if __name__ == '__main__':
    
    
    car = Car('Ferrari', 100, True)
    bike = Bike('Royal Enfield', 40, True)
    bus = Bus("Yutong", 500, True)
    vehicle = Vehicles()


    while True:

        print(f"""
    1.Show Vehicles
    2.Rent
    3.Return
    4.Bill
    5.Exit
            """)
        choice = input('Choose any\n=')

        if choice == '1':
            vehicle.show_vehicles()
        elif choice == '2':
            vehicle.rent_vehicle()
        elif choice == '3':
            vehicle.return_vehicles()
        elif choice == '4':
            vehicle.bill()
        elif choice == '5':
            break
            
        



        

