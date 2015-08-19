__author__ = 'mw'

import unittest
from angry_dice import AngryDice
from unittest.mock import patch
from io import StringIO


class TestAngryDicePrintResults(unittest.TestCase):

    def setUp(self):
        """ Initializes the die for the following testing functions """
        self.game = AngryDice()
        # print(self.shortDescription())

    def tearDown(self):
        """ delete the instance of game after running tests """
        del self.game

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_results(self, mock_stdout):
        """ initialize and test the output """
        self.game.stage = 1
        self.game.die_a = "2"
        self.game.die_b = "3"
        self.game.outcome = "This is a Test"
        output = "\nYou are in Stage {}\n" \
                 "-------------------------------\n" \
                 "You rolled:\n" \
                 "a = [  {}  ]\n" \
                 "b = [  {}  ]\n" \
                 "{}".format(1, "2", "3", "This is a Test\n")
        self.game.print_results()
        self.assertMultiLineEqual(mock_stdout.getvalue(), output,
                                  "output matches the print_results format")


if __name__ == '__main__':
    unittest.main()
