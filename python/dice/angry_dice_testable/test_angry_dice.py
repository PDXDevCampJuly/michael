__author__ = 'mw'

import unittest
from dice_class import Die
from angry_class import AngryDice


class AngryDiceTest(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, True)


    def setUp(self):
        """ Initializes the die for the following testing functions """

        self.die_a = Die(["a", "b", "ANGRY", "c", "d", "e"])
        self.die_b = Die(["a", "b", "ANGRY", "c", "d", "e"])

        print(self.shortDescription())

    def test_instructions_output(self):
        instructions("hello")


if __name__ == '__main__':
    unittest.main()
