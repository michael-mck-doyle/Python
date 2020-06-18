
# collect user input
user_input = input("Enter your senetence: ")
#mock_input = "squad helps dog bit victim"
#input_2 = "gator attack puzzles experts"

# functionality to capitalise each word

def titlecase(text):
    titlecase = []
    for word in text.split():
        cap_word = word.capitalize()
        titlecase.append(cap_word)
    return " ".join(titlecase)

#print(titlecase(mock_input))
#print(titlecase(input_2))

x = (titlecase(user_input))
print(x)


