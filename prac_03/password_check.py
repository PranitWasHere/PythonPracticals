MINIMUM_LENGTH = 6


def get_password(minimum_length):
    password = input("Enter the password: ")
    while len(password) < minimum_length:
        print(f"Password needs to be at least {minimum_length} characters")
        password = input("Enter the password: ")
    return password


def print_asterisks(asterisks):
    print('*' * len(asterisks))


def main():
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


if __name__ == '__main__':
    main()