from prac_08.unreliable_car import UnreliableCar

def main():
    car_test = UnreliableCar("Lemon", 100, 60)
    print(car_test)
    car_test.drive(40)
    print(car_test)

main()