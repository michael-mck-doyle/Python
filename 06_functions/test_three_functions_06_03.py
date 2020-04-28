import unittest
import three_functions_06_03


class NestedFunctions(unittest.TestCase):
    """example showing functions arguments of functions"""
    def test_funcs(self):
        self.assertEqual(three_functions_06_03.a_func(4), 5)

    def test_houses(self):
        self.assertEqual(three_functions_06_03.house_sales(600, 5000), 3000000)


if __name__ == '__main__':
    unittest.main()