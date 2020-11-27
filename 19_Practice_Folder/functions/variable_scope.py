glob = 2

# you can use the ""variable_name" in globals()" to confirm if a variable is indeed a global variable
print("glob" in globals())

# you can use the ""variable_name" in locals()" to confirm if a variable is indeed a local variable i.e. only available
# within a function


def fun():
    loc = 2
    print("glob" in locals())
    print("loc" in locals())
    print("loc" in globals())


fun()

print()
print()

name = "Harry"
print(name)


def names():
    name2 = "Sally"
    print(name)
    print(name2)


names()


###
