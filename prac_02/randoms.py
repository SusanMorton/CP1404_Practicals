import random

print(random.randint(5,20))
#line1: smallest number is 5, largest number is 20

print(random.randrange(3,10,2))
#line2: smallest number is 3, largest number is 9. Could not produce 4 as its step 2 from 3 (3, 5, 7, 9)

print(random.uniform(2.5,5.5))
#line3: smallest number is 2.5, largest number is 5.5, seems to be similar to randit, except it produces floats between the range numbers instead of ints


print(random.randint(1,100))