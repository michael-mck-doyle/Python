import unittest
import run_it


class RunIt(unittest.TestCase):
    """test number of seconds """
    def test_calc_secs(self):
        self.assertEqual(run_it.calc_secs(1, 365, 24, 60, 60), 31536000)


if __name__ == '__main__':
    unittest.main()