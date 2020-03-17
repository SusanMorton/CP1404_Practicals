import random

def main():
    MIN_VALUE = 1
    MAX_VALUE = 45
    NUM_PER_LINE = 6

    number_list = []
    numbers_of_lines = int(input("How many quick picks? " ))

    for number_of_lines in range(numbers_of_lines):
        individual_number_list = []
        #individual_number_list = [number for number in range(6) not in individual_number_list]
        valid_number = 0
        for i in range(NUM_PER_LINE):
            while valid_number !=NUM_PER_LINE:
                number = random.randint(MIN_VALUE,MAX_VALUE)
                print("current list is {}".format(individual_number_list))
                if number not in individual_number_list:
                    individual_number_list.append(number)
                    valid_number +=1
                else:
                    print("invalid number {}".format(number))
        print("successful list: {}".format(individual_number_list))
        number_list.append(individual_number_list)
    print(number_list)
    



main()