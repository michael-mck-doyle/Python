'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

all_words = []

with open('words.txt', 'r') as fin:
    for word in fin.readlines():
        #all_words.append(word)
        all_words.append(word.rstrip("\n"))

with open('words_reverse.txt', 'w') as f_out:
    for word in all_words:
        all_words.reverse()
    f_out.write(str(all_words))




