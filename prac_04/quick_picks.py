import random

def main():

    number_list = []
    numbers_of_lines = int(input("How many quick picks? " ))

    for number_of_lines in range(numbers_of_lines):
        individual_number_list = []
        for i in range(6):
            number = random.randint(1,45)
            individual_number_list.append(number)
        print(individual_number_list)
        number_list.append(individual_number_list)
    print(number_list)



main()