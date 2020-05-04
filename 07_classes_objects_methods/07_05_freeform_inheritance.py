'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''


class Drink:
    def __init__(self, size):
        self.size = size


class FizzyDrink(Drink):
    def __init__(self, size, bubbles):
        super().__init__(size)
        self.bubbles = bubbles


class Beer(FizzyDrink):
    def __init__(self, size, bubbles, alcoholic):
        super().__init__(size, bubbles)
        self.alcoholic = alcoholic

    def __repr__(self):
        return f"My drink order is {self.size} mls of alcoholic {self.alcoholic} bubbles {self.bubbles}"


print()
halfPint = Beer(330, True, True)
print(halfPint)

