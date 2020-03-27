
word_dict = {}
#userwords = input('Text: ')
userwords = "this is a colletion of words of nice words this is a fun thing it is"
for word in userwords.split():
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

print(word_dict)

for words,count in word_dict.items():
    print("{} : {}".format(words, count))

word_list = []

for singleword in word_dict:
    word_list.append(singleword)

print(word_list)
word_list.sort()
print(word_list)

max_word_length = max(len(word) for word in word_list)
print(max_word_length)
