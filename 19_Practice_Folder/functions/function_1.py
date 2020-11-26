
mock_input = "hello hello my name's dibo"

def titlecase(text):
    titlecase = []
    for word in mock_input.split():
        word = word.capitalize()
        titlecase.append(word)

    print(titlecase)
    return " ".join(titlecase)


#user_input = input("input a phrase: ")

print(titlecase(mock_input))

