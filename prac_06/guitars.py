"""Stores information about users guitars"""

from prac_06.guitar import Guitar

def main():
    guitars = []
    print("My guitars: ")
    stop_ind = 0
    while stop_ind != 1:
        name = input("Name: ")
        if name == "":
            stop_ind = 1
        else:
            year = int(input("Year: "))
            cost = int(input("Cost: "))
            guitars.append(Guitar(name, year, cost))
            print("{} ({}) : ${:.2f} added \n".format(name, year, cost))


    print(guitars)

main()