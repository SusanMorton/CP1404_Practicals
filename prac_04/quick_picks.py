import random

def main():

    number_list = []
    numbers_of_lines = int(input("How many quick picks? " ))

    for number_of_lines in range(numbers_of_lines):
        individual_number_list = []
        #individual_number_list = [number for number in range(6) not in individual_number_list]
        valid_number = 0
        for i in range(6):
            while valid_number !=6:
                number = random.randint(1,45)
                print("current list is {}".format(individual_number_list))
                if number not in individual_number_list:
                    individual_number_list.append(number)
                    valid_number +=1
                else:
                    print("invalid number {}".format(number))
        print(individual_number_list)
        number_list.append(individual_number_list)
    print(number_list)



main()