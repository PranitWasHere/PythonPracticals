from silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(60)
    print(taxi)
    print(taxi.get_fare())
    taxi_hummer = SilverServiceTaxi("Hummer", 200, 4)
    taxi_hummer.drive(0)
    print(taxi_hummer)

if __name__ == '__main__':
    main()