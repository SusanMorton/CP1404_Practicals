from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    test_ride = SilverServiceTaxi("Hummer", 100, 2)
    print(test_ride)
    test_ride.drive(18)
    print("That drive costs ${:.2f}".format(test_ride.get_fare()))
    print(test_ride)


main()