import random

def main():

    number_list = []
    numbers_of_lines = int(input("How many quick pick lines do you want?:" ))
    valid_numbers = 0
    for number_of_lines in range(numbers_of_lines):
        number_generator = random.randint(1,45)
        if number_generator in number_list:
            print("invalid number {}".format(number_generator))
            #number_generator = random.randint(1, 45)
            #print("new number {}".format(number_generator))
        else:
            print(number_generator)
            number_list.append(number_generator)
            print(number_list)
            valid_numbers +=1

main()