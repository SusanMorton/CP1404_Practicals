
numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0]) #will equal 3
print(numbers[-1]) #will equal 2
print(numbers[3]) #will equal 1
print(numbers[:-1]) #will remove the final number (2) and print the remaining list
print(numbers[3:4]) #will print 1 -- what does :4 do ??
print(5 in numbers) #will equal 9 -- incorrect, will look for a 5 and print true
print(7 in numbers)# will equal false, as no 7 in numbers
print("3" in numbers) # will equal false as no string 3 in numbers
print(numbers + [6, 5, 3]) # will add the [6,5,3] into the list

