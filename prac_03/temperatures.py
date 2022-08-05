"""
CP1404 - Practical
Pseudocode for temperature conversion
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print(to_fahrenheit())
        elif choice == "F":
            print(to_celsius())
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9 / 5 + 32
    return "Result: {:.2f} F".format(fahrenheit)


def to_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return f"Result: {round(celsius, 2)} C"


if __name__ == '__main__':
    main()