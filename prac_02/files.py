name_file = open("name.txt", "w")

users_name = input("What is your name?")

print("Your name is {}".format(users_name),file=name_file)

name_file.close()

name_file = open("name.txt", "r")

first_line = name_file.readline()

print(first_line)

name_file.close()


file = open("numbers.txt", "r")
number_one = int(file.readline())
number_two = int(file.readline())
print(number_one)
print(number_two)
result = number_one + number_two
print(result)

file.close()

file = open("numbers.txt", "r")
result_two = 0
for lines in file:
    num_one = int(lines)
    result_two = num_one + result_two

print(result_two)

file.close()