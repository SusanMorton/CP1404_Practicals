from prac_08.carv2 import Car
import random

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        super().drive(distance)
        random_number = random.randint(0, 100)
        if random_number < self.reliability:
            distance = distance
        elif random_number > self.reliability:
            distance = 0
            self.odometer = 0
        return distance