__author__ = 'Chelsea | Michael'

import unittest
from Conect4_View import View
from unittest.mock import patch
from io import StringIO


class TestModelShowTurn(unittest.TestCase):
    """ Checks the visual aspect of the user knowing whose turn. """

    def setUp(self):
        """Inits empty grid for testing"""
        self.theView = View()

    def tearDown(self):
        """ Closes the view """
        del self.theView

    @patch('builtins.input', return_value='2')
    def test_show_turn_player_a_keyboard_input_2(self, input_value):
        """ Check if keyboard input 2 works """
        move = self.theView.show_turn(["Player_A"])

        self.assertEqual(move, 1)

    @patch('builtins.input', side_effect=['a','2'])
    def test_show_turn_player_a_keyboard_input_a(self, input_value):
        move = self.theView.show_turn(["Player_A"])
        """ Check if keyboard input a works """

        self.assertEqual(move, 1)

    @patch('builtins.input', side_effect=['','2'])
    def test_show_turn_player_a_keyboard_input_blank(self, input_value):
        """ Check if blank keyboard input works """
        move = self.theView.show_turn(["Player_A"])

        self.assertEqual(move, 1)

    @patch('builtins.input', side_effect=['9','2'])
    def test_show_turn_player_a_keyboard_input_9(self, input_value):
        """ Check if keyboard input 9 works """
        move = self.theView.show_turn(["Player_A"])

        self.assertEqual(move, 1)


if __name__ == '__main__':
    unittest.main()
