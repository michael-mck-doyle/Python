


class Ingredient:
    def __init__(self, name, colour, amount):
        self.name = name
        self.colour = colour
        self.amount = amount

    def __str__(self):
        return f"You have {self.amount} {self.colour} {self.name}."

    def __repr__(self):
        return f"{self.name} is the name of this object"

    def use(self, use_amount):
        self.amount -= use_amount


i = Ingredient(name='carrot', colour='orange', amount=12)
print(i)

print(i.name, i.colour, i.amount)

c = Ingredient('cabbage', 'green', 15)

print(c)

print(c.name, c.colour, c.amount)


i.use(3)
print(i.amount)


class Ingredient:
  """Models an ingredient including its name and amount."""
  def __init__(self, name, amount):
    self.name = name
    self.amount = amount

  def __str__(self):
    return f"There are {self.amount} of {self.name}."

  def use(self, use_amount):
    """Reduces the amount of ingredient available."""
    self.amount -= use_amount

  def expire(self):
    """Expires the ingredient item."""
    print(f"whoops, these {self.name} went bad...")
    self.name = "expired " + self.name


# INHERITANCE: building a subclass called Spice


class Spice(Ingredient):
  """Models an ingredient including its name, amount, and taste."""
  # customize the __init__() method
  def __init__(self, name, amount, taste):
    super().__init__(name, amount)
    self.taste = taste

  # create a custom method grind()
  def grind(self):
    print(f"you have now {self.amount} of ground {self.name}")

  # override the expire() method
  def expire(self):
    if self.name == 'salt':
      print(f"{self.name} never expires! ask the sea!")
    else:
      print(f"this {self.name} went bad...")
      self.name = f"expired {self.name}"
