'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

list_before = ['a', 'e', 'i', 'o', 'u']
list_after = []
r = (input("Please enter a string of words: "))
r = (r.lower())

vowels = 0
count_vowels = 0
for x in list_before:
    if x in r:

        vowels = r.count(x)
        print(x, " = ", vowels)
        count_vowels = count_vowels + vowels
        list_after.append(x)

    elif x not in r:
        print(x, "is not in the string")

    else:
        print("There are no more vowels to count")

missing_vowel = set(list_before)-set(list_after)

print("The vowels present in the string are" + str(list_after))
print("The total Number of Vowels in this String = ", count_vowels)

print("Vowels not present in the string is/are: " + str(missing_vowel))

