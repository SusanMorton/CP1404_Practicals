def main():

    minimum_length = 6
    password = get_password(minimum_length)

    print_asterisks(password)


def print_asterisks(password):
    for char in password:
        print("*", end='')


def get_password(minimum_length):
    password = input("Enter a password")
    valid_password = False
    while not valid_password:
        if len(password) < minimum_length:
            password = input("Enter a password")
        else:
            valid_password = True
    return password


main()
