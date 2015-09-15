__author__ = 'Chelsea'

import unittest
from Tokyo_monster_game import Monster

class Check_heal(unittest.TestCase):

    def setUp(self):
        self.monster = Monster()

    def tearDown(self):
        del self.monster

    def test_if_heal_works_under_ten(self):

        self.monster.health = 3

        self.monster.heal(5)

        self.assertEqual(self.monster.health, 8)


    def test_if_heal_works_above_ten(self):

        self.monster.health = 6

        self.monster.heal(5)

        self.assertEqual(self.monster.health, 10)


if __name__ == '__main__':
    unittest.main()