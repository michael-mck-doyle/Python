#import yourpackage
import unittest
import math  # use the code you want to test instead

'''
class TestYourPackage(unittest.TestCase, yourpackage):
    def __init__(self):
        super().__init__()
        pass
'''


class TestMath(unittest.TestCase):
    def test_floor_rounds_down(self):
        self.assertEqual(math.floor(3.4), 3)
        if __name__ == '__main__':
            unittest.main()




