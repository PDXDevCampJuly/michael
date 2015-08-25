__author__ = 'Chelsea'

import unittest
from Tokyo_monster_game import Monster



class Check_stats_when_reset(unittest.TestCase):

    def setUp(self):
        self.monster_game = Monster()

    def tearDown(self):
        del self.monster_game

    def test_stats(self):
        self.monster_game.currentstage = 2
        self.monster_game.health = 3
        self.monster_game.victory_points = 2

        self.monster_game.reset()

        self.assertEqual(self.monster_game.current_status, 1)
        self.assertEqual(self.monster_game.health, 10)
        self.assertEqual(self.monster_game.victory_points, 0)

    def test_stats(self):
        self.monster_game.currentstage = 25
        self.monster_game.health = 60
        self.monster_game.victory_points = 60

        self.monster_game.reset()

        self.assertEqual(self.monster_game.current_status, 1)
        self.assertEqual(self.monster_game.health, 10)
        self.assertEqual(self.monster_game.victory_points, 0)
if __name__ == '__main__':
    unittest.main()
