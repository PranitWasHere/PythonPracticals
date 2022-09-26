from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def display_taxis(taxis):
    print('Taxis available: ')
    for i in range(len(taxis)):
        print(f"{i} - {taxis[i]}")


MENU = '''q)uit, c)hoose taxi, d)rive'''


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    taxi = None
    bill_to_date = 0
    print("Let's drive!")
    while True:
        print(MENU)
        choice = input().lower()
        if choice not in 'cdq':
            print('Invalid option')
        elif not taxi and choice == 'd':
            print("You need to choose a taxi before you can drive")
        elif choice == 'c':
            display_taxis(taxis)
            choice_taxi = input("Choose taxi: ")
            if choice_taxi.isnumeric():
                choice_taxi = int(choice_taxi)
                if choice_taxi < len(taxis):
                    taxi = taxis[choice_taxi]
                else:
                    print("Invalid taxi choice")
            else:
                print("Invalid taxi choice")
        if choice == 'd' and taxi is not None:
            try:
                distance = int(input("Drive how far? "))
            except ValueError:
                print("Invalid Input")
                continue
            taxi.start_fare()
            taxi.drive(distance)
            print(f"Your {taxi.name} trip cost you ${taxi.get_fare():<.2f}")
            bill_to_date += taxi.get_fare()
        print(f"Bill to date ${bill_to_date:.2f}")


if __name__ == "__main__":
    main()
