import unittest
import stats_06_02


class TestRndmNumStats(unittest.TestCase):
    """ test stats function"""
    def test_list_type(self):
        self.addTypeEqualityFunc(list, stats_06_02.ran_list)

    def test_stat(self):
        self.assertEqual(stats_06_02.stats([51, 10, 83, 65, 47, 18, 27, 30, 79, 49, 34, 22, 92, 70, 23, 49, 47, 1, 89, 3]), (92, 1, 44.45, 889))


if __name__ == '__main__':
    unittest.main()
