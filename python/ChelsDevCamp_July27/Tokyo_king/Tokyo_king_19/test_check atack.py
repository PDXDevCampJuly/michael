__author__ = 'Chelsea'

import unittest
from Tokyo_monster_game import Monster

class Check_attack(unittest.TestCase):

    def setUp(self):
        self.monster = Monster()

    def tearDown(self):
        del self.monster

    def test_subtraction_works(self):

        self.monster.health = 3

        self.monster.attack(5)

        self.assertNotEqual(self.monster.health, 3)

if __name__ == '__main__':
    unittest.main()
