__author__ = 'Chelsea'

import unittest
from Tokyo_monster_game import Monster

class Check_in_tokyo(unittest.TestCase):

    def setUp(self):
        self.monster_game = Monster()

    def tearDown(self):
        del self.monster_game

    def test_if_in_tokyo(self):
        self.monster_game.current_status, 1

        self.monster_game.in_tokyo()

        self.assertFalse(self.monster_game.In_Tokyo, False)


if __name__ == '__main__':
    unittest.main()
