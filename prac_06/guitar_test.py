"""Tests the guitar class"""

from prac_06.guitar import Guitar

def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another guitar", 2013, 100)

    print(gibson)

    print("Gibson L-5 CES get_age() - Expected 98. Got {}".format(gibson.get_age()))
    print("Another guitar get_age() - Expected 7. Got {}".format(another_guitar.get_age()))
    print("Gibson L-5 CES is_vintage() - Expected True. Got {}".format(gibson.is_vintage()))
    print("Another guitar is_vintage() - Expected False. Got {}".format(another_guitar.is_vintage()))



main()