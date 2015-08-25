__author__ = 'Chelsea'

import unittest
from angry_dice import Angry_dice


class CheckForCheatingTest(unittest.TestCase):
    """Tests if cheat will re-roll for you if you try to hold a six"""

    def setUp(self):
        self.angry_game = Angry_dice()

    def tearDown(self):
        del self.angry_game

    def test_check_cheating_six_and_six(self):
        self.angry_game.die_a.currentValue = "6"
        self.angry_game.die_b.currentValue = "6"
        self.angry_game.roll = ''
        self.angry_game.current_stage = 3

        self.angry_game.is_cheat(self.angry_game.roll)

        self.assertTrue(self.angry_game.is_cheat, True)

    def test_check_cheating_two_and_six(self):
        self.angry_game.die_a.currentValue = "2"
        self.angry_game.die_b.currentValue = "6"
        self.angry_game.roll = ''
        self.angry_game.current_stage = 3

        self.angry_game.is_cheat(self.angry_game.roll)

        self.assertTrue(self.angry_game.is_cheat, True)

    def test_check_cheating_two_and_five(self):
        self.angry_game.die_a.currentValue = "2"
        self.angry_game.die_b.currentValue = "5"
        self.angry_game.roll = ''
        self.angry_game.current_stage = 3

        self.angry_game.is_cheat(self.angry_game.roll)

        self.assertTrue(self.angry_game.is_cheat, False)

if __name__ == '__main__':
    unittest.main()




