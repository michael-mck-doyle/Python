import unittest
import rock_paper_scissors


class TestGame(unittest.TestCase):
    """ tests to ensure the rock, paper, scissors game works as expected"""
    def test_user_rps(self):
        self.assertEqual(rock_paper_scissors.get_user_hand(1), "paper")
        self.assertEqual(rock_paper_scissors.get_user_hand(2), "paper")

    def test_comp_rps(self):
        self.assertEqual(rock_paper_scissors.get_comp_hand(1), "paper")
        self.assertEqual(rock_paper_scissors.get_comp_hand(2), "paper")


if __name__ == '__main__':
    unittest.main()
