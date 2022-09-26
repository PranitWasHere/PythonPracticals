from taxi import Taxi


def main():
    # 1.
    taxi = Taxi("Prius 1", 100)
    # 2.
    taxi.drive(40)
    # 3.
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")
    print()
    # 4.
    taxi.start_fare()
    print("===== New Trip =====")
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")

    actual_distance_driven = taxi.drive(100)
    print(f"After attempting to drive 100km... actual {actual_distance_driven}")
    # 5.
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")


if __name__ == '__main__':
    main()