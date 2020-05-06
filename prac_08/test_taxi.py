from prac_08.carv2 import Car
from prac_08.taxi import Taxi

def main():
    taxi = Taxi("Prius 1", 100)
    print(taxi)
    taxi.drive(40)
    print(taxi)
    print("Current fare ${:.2f}".format(taxi.get_fare()))
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)
    print("Current fare ${:.2f}".format(taxi.get_fare()))

main()