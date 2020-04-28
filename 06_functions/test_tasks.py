import unittest
import tasks_06_01


class TestTasks(unittest.TestCase):
    """ docstrings"""
    def test_div4or7(self):
        self.assertEqual(tasks_06_01.mod4_or_7(7), True)
        self.assertEqual(tasks_06_01.mod4_or_7(3), False)

    def test_dic4and7(self):
        self.assertEqual(tasks_06_01.mod4_and_7(28), True)
        self.assertEqual(tasks_06_01.mod4_and_7(14), False)
        self.assertEqual(tasks_06_01.mod4_and_7(5), False)


if __name__ == '__main__':
    unittest.main()

