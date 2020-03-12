MIN_LENGHT = 6

password = input("Enter a password")
valid_password = False

while not valid_password:
    if len(password) < MIN_LENGHT:
        password = input("Enter a password")
    else:
        valid_password = True

for char in password:
    print("*", end='')

