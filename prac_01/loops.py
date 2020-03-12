for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

user_chosen_number= int(input("Choose an integer number: "))
for i in range(user_chosen_number):
    print('*', end=' ')
print()

for i in range(1, user_chosen_number + 1):
    print('*' * i)





