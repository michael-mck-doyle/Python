'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.

'''

all_words = []
more_words = []
shortest_words = []
longest_words = []

with open('words.txt', 'r') as fin:
    for word in fin.readlines():
        all_words.append(word)

    for word in all_words:
        #word.rstrip("\n")
        more_words.append(word.rstrip("\n"))

    longest = max(more_words, key=len)
    shortest = min(more_words, key=len)

    for word in more_words:
        if len(word) == len(longest):
            longest_words.append(word)

    for word in more_words:
        if len(word) == len(shortest):
            shortest_words.append(word)


    print(f"There are {len(more_words)} words in the file")
    print(f"The {len(shortest_words)} shortest word(s) with {len(shortest_words[0])} characters in the file are {shortest_words}")
    print(f"The {len(longest_words)} longest word(s) with {len(longest_words[0])} characters in the file are {longest_words}")
