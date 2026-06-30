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

    @abstractmethod
    def rent(self):
        if self.__available:
            self.__available = False
            print('Successfully rented')
        else:
            print('Sorry not available to rent')

    @abstractmethod
    def return_vehicle(self):
        if not self.__available:
            self.__available = True
            print('Returned Successfully')
        else:
            print('Not rented at all')

    @abstractmethod
    def calculate_bill(self):
        days = int(input('How many days rent for?\n='))
        total_bill = days * self.rent_per_day
        print(f'Your Total bill is, ${total_bill}')


class Car(Vehicle):
    def __init__(self, name, rent_per_day, available):
        super().__init__(name, rent_per_day, available)
        self.rent_per_day = int(rent_per_day - ((rent_per_day*5)/100)) # Using Int for avoiding fractions, here 5% discount is applied

    def rent(self):
        super().rent()

    def return_vehicle(self):
        super().return_vehicle()
    
    def calculate_bill(self):
        super().calculate_bill()

class Bike(Vehicle):
    def __init__(self, name, rent_per_day, available):
        super().__init__(name, rent_per_day, available)

    def rent(self):
        super().rent()
        
    def return_vehicle(self):
        super().return_vehicle()
    
    def calculate_bill(self):
        super().calculate_bill()

class Bus(Vehicle):
    def __init__(self, name, rent_per_day, available):
        super().__init__(name, rent_per_day, available)
        self.rent_per_day = int(rent_per_day - ((rent_per_day*10)/100))# Using Int for avoiding fractions, here 10% discount is applied

    def rent(self):
        super().rent()

    def return_vehicle(self):
        super().return_vehicle()

    def calculate_bill(self):
        super().calculate_bill()

class Vehicles:
    def __init__(self):
        self.vehicles = [car, bike, bus]

    def show_vehicles(self):
        for vehicle in self.vehicles:
            if isinstance(vehicle, Car):
                print(f'Type: Car, Brand: {vehicle.name}, Rent: {vehicle.rent_per_day}\Day, Available: {vehicle.get_available()}')
            if isinstance(vehicle, Bike):
                print(f'Type: Bike, Brand: {vehicle.name}, Rent: {vehicle.rent_per_day}\Day, Available: {vehicle.get_available()}')
            if isinstance(vehicle, Bus):
                print(f'Type: Bus, Brand: {vehicle.name}, Rent: {vehicle.rent_per_day}\Day, Available: {vehicle.get_available()}')

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
            car.calculate_bill()
        if vehicle_type == '2':
            bike.calculate_bill()
        if vehicle_type == '3':
            bus.calculate_bill()

        
    
   



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
            
        



        

