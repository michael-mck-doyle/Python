'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

# References
# 7.2. Reading and Writing Files - https://docs.python.org/3/tutorial/inputoutput.html


# To write to a file you must first open the file in write mode.  Using "w" will overwrite anything currently within the file.
fout = open('output.txt', 'w')

# We can then write data to the file "output.txt" using the write() method
fout.write('Writing to a file for the first time')

# Lastly, it is important to always close the file after opening:
fout.close()

# using "a" appends new data to the file
f = open("output.txt", "a")
f.write(". That wasn't so bad!")
f.close()


# Reading from Files
# First, we have to open the file in read mode:
fin = open('input.txt', 'r')

# We can then use one of the many read methods python provides.
# The read() method reads the entire file and returns the contents as a string. For example:
contents = fin.read()

# don't forget to close the file
fin.close()

# using "with"
with open("output.txt", "r") as fin:
    for line in fin.readline():

with open('input.txt', 'r') as fin:
    print(fin.readline())
