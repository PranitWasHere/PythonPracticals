from unreliable_car import UnreliableCar


def main():
    good_car = UnreliableCar("good", 100, 90)
    bad_car = UnreliableCar("bad", 100, 9)

    for i in range(1, 12):
        print(f"Attempting to drive {i}km")
        print(f"{good_car.name} drove {good_car.drive(i)}km")
        print(f"{bad_car.name} drove {bad_car.drive(i)}km")

    print(good_car)
    print(bad_car)


if __name__ == '__main__':
    main()