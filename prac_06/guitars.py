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
            cost = float(input("Cost: "))
            guitars.append(Guitar(name, year, cost))
            print("{} ({}) : ${:.2f} added \n".format(name, year, cost))
    #guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    #guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars: ")
    for i, guitar in enumerate(guitars):
        guitar.get_age()
        guitar.is_vintage()
        if guitar.is_vintage() == True:
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print("Guitar {}: {:<20} ({}), worth ${:10,.2f} {}".format(i+1, guitar.name, guitar.year, guitar.cost, vintage_string))


main()