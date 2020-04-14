'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}
dict_3 = {}

dict_3.update(dict_1)
dict_3.update(dict_2)
print(dict_3)

for x in dict_1:
    if x in dict_2:
        dict_3[x] = dict_1[x] + dict_2[x]
    else:
        pass

print(dict_3)

