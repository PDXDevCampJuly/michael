__author__ = 'Chelsea'

import unittest
from Tokyo_monster_game import Monster

class Check_stats_when_reset(unittest.TestCase):

    def setUp(self):
        self.monster_game = Monster()

    def tearDown(self):
        del self.monster_game

    def test_stats(self):
        """If the currentstage is 2, the health is 3 and the victory points are 2.
        if you call reset it should reset to the starting stats"""
        self.monster_game.currentstage = 2
        self.monster_game.health = 3
        self.monster_game.victory_points = 2

        self.monster_game.reset()

        self.assertEqual(self.monster_game.current_status, 1)
        self.assertEqual(self.monster_game.health, 10)
        self.assertEqual(self.monster_game.victory_points, 0)

    def test_stats(self):
        """
        Same as above but with numbers tha you shouldn't be able to have
        """
        self.monster_game.currentstage = 25
        self.monster_game.health = 60
        self.monster_game.victory_points = 60

        self.monster_game.reset()

        self.assertEqual(self.monster_game.current_status, 1)
        self.assertEqual(self.monster_game.health, 10)
        self.assertEqual(self.monster_game.victory_points, 0)
if __name__ == '__main__':
    unittest.main()
