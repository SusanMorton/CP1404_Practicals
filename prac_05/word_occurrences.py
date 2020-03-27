
word_counter = {}
usertext = input('Enter a sentence here: ')

for word in usertext:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

print(word_counter)