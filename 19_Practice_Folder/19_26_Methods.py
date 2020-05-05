"""
__ References __

The definitive guide on how to use static, class or abstract methods in Python - https://julien.danjou.info/guide-python-static-class-abstract-methods/

"""


class Pizza(object):
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size


print(Pizza.get_size(Pizza(42)))







