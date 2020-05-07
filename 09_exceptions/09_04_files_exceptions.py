'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''


try:

    war = []
    crime = []
    pride = []
    x = []
    y = []
    z = []

    with open('/Users/Michael/Documents/CodingNomads_Python/labs/09_exceptions/books/war_and_peace.txt', 'r') as fin:
        #word = fin.readlines()
        for word in fin.readlines():
            war.append(word)
        #print(war)
        x = war[0][1]
        print(f"The first character in 'War and Peace' is '{x}'. ")

    with open('/Users/Michael/Documents/CodingNomads_Python/labs/09_exceptions/books/pride_and_prejudice.txt', 'r') as fin:
        for word in fin.readlines():
            pride.append(word)
        #print(pride)
        z = pride[0][1]
        print(f"The first character in 'Pride and Prejudice' is '{z}'.")

    with open('/Users/Michael/Documents/CodingNomads_Python/labs/09_exceptions/books/crime_and_punishment.txt', 'w') as fout:
        fout.write('')

    with open('/Users/Michael/Documents/CodingNomads_Python/labs/09_exceptions/books/crime_and_punishment copy.txt', 'r') as fin:
        for word in fin.readlines():
            crime.append(word)
        #print(crime)
        y = crime[0][1]
        print(f"The first character in 'Crime and Punishment' is '{y}'.")


except FileNotFoundError as e:
    print("File was not found", e)
except NameError as e:
    print("File import name error", e)
except ValueError as e:
    print("The file has already been closed.", e)
except TypeError as e:
    print(e)
except KeyboardInterrupt as e:
    print("User stopped program.")
except IndexError as e:
    print("Check List for errors.", e)



