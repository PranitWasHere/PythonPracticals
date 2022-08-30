"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    # 1
    limo = Car(fuel=100)
    # 2
    limo.add_fuel(20)
    # 3
    print(f" fuel = {limo.fuel}")
    # 4
    distance_driven = limo.drive(115)
    # 5
    print(f" Actual distance travelled = {distance_driven}")
    print(f" odometer = {limo.odometer}")

    distance_driven = limo.drive(200)
    print(f" Actual distance travelled = {distance_driven}")
    print(f" odometer = {limo.odometer}")

    # 6
    print(str(limo))

    # 7
    mustang = Car(name= "Mustang", fuel= 200)

    # 8
    print(str(mustang))

main()