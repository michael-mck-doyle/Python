'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

gen = (x for x in range(1, 101) if x % 3 == 0)

print(gen)

for g in gen:
    print(g)
