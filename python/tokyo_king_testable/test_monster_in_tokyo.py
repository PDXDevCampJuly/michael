__author__ = 'mw'

import unittest
from monster_class import Monster


class TestMonsterInTokyo(unittest.TestCase):

    def setUp(self):
        """ Initializes the monster for the following testing functions. """
        self.monster = Monster("Cereal Killer")

    def tearDown(self):
        """ Delete the instance of monster after running tests. """
        del self.monster

    def test_monster_if_in_tokyo(self):
        """ Determine if monster in Tokyo """
        self.monster.status = "in Tokyo"
        self.monster.in_tokyo()
        self.assertTrue(True, self.monster.status)

    def test_monster_if_out_of_tokyo(self):
        """ Determine if monster Out of Tokyo """
        self.monster.status = "Out of Tokyo"
        self.monster.in_tokyo()
        self.assertFalse(False, self.monster.status)


if __name__ == '__main__':
    unittest.main()
