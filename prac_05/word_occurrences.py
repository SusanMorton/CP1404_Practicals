
word_dict = {}
userwords = input('Text: ')
# userwords = "this is a colletion of words of nice words this is a fun thing it is"
"""counting the words in the text string and inserting into dictionary"""
for word in userwords.split():
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

# print(word_dict)
"""formatting keys/values in dictionary to print"""
for words, count in word_dict.items():
    print("{} : {}".format(words, count))

word_list = []
"""sorting keys into a new list"""
for singleword in word_dict:
    word_list.append(singleword)
word_list.sort()
# print(word_list)

"""counting the maximum length of words in the word list"""
max_word_length = max(len(word) for word in word_list)
# print(max_word_length)


"""formatting words/values in dictionary to print with alignment"""
for word in word_list:
    print("{:{}} : {}".format(word, max_word_length, word_dict[word]))
