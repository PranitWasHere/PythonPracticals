import random

MINIMUM = 1
MAXIMUM = 45
NUMBER_OF_LINE = 6


def main():
    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks <= 0:
        print("Please enter a number > than 0")
        number_of_picks = int(input("How many quick picks? "))

    for i in range(number_of_picks):
        quick_pick = []
        for j in range(NUMBER_OF_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()