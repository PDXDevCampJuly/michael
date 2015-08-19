__author__ = 'mw'

import unittest
from monster_class import Monster


class TestMonsterScore(unittest.TestCase):

    def setUp(self):
        """ Initializes the monster for the following testing functions """
        self.monster = Monster("Cereal Killer")

    def tearDown(self):
        """ delete the instance of monster after running tests """
        del self.monster

    # def test_something(self):
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
