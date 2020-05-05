'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

all_words = []
long_words = []

with open('words.txt', 'r') as fin:
    #for word in fin.readlines():
    #for word in fin:
     #   all_words.append(word)
    #for word in all_words:
    for word in fin:
        if len(word) > 20:
            long_words.append(word)


#print(all_words[0:])

print(long_words[0:])

