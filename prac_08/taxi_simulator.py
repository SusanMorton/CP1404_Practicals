from prac_08.carv2 import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose, d)rive"

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    current_bill = 0
    print("Let's Drive!")
    print(MENU)
    menu_choice = input(">>>>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis Available")
            choose_taxi(taxis)
            chosen_taxi = int(input("Choose taxi: "))
            current_taxi = taxis[chosen_taxi]
            print("Bill to date: ${:.2f}".format(current_bill))
            print(MENU)
            menu_choice = input(">>>>> ").lower()

        elif menu_choice == "d":
            distance = int(input("Drive how far?"))
            current_taxi.drive(distance)

            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
            current_bill += current_taxi.get_fare()
            print("Bill to date: ${:.2f}".format(current_bill))

            print(MENU)
            menu_choice = input(">>>>> ").lower()


    if menu_choice == "q":
        choose_taxi(taxis)

def choose_taxi(taxis):
    for i, taxi in enumerate(taxis):
        print(i, "-", taxi)

main()