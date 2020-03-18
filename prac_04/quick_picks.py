import random

def main():
    MIN_VALUE = 1
    MAX_VALUE = 45
    NUM_PER_LINE = 6

    numbers_of_lines = int(input("How many quick picks? "))

    for number_of_lines in range(numbers_of_lines):
        individual_number_list = []
        valid_number = 0
        for i in range(NUM_PER_LINE):
            while valid_number !=NUM_PER_LINE:
                number = random.randint(MIN_VALUE,MAX_VALUE)
                if number not in individual_number_list:
                    individual_number_list.append(number)
                    valid_number +=1
        individual_number_list.sort()
        print("{:>3} {:>3} {:>3} {:>3} {:>3} {:>3}".format(*individual_number_list))


main()