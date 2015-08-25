__author__ = 'Chelsea | Michael'

import unittest
from Conect4_View import View
from unittest.mock import patch
from io import StringIO


class TestModelShowTurn(unittest.TestCase):
    """make sure it prints an empty list"""

    def setUp(self):
        """Inits empty grid for testing"""
        self.theView = View()

    def tearDown(self):
        """ Closes the view """
        del self.theView

    @patch('builtins.input', return_value='2')
    def test_show_turn_player_a(self, input_value):
        move = self.theView.show_turn(["Player_A"])

        self.assertEqual(move, 1)

    @patch('builtins.input', side_effect=['a','2'])
    def test_show_turn_player_a(self, input_value):
        move = self.theView.show_turn(["Player_A"])

        self.assertEqual(move, 1)

    @patch('builtins.input', side_effect=['','2'])
    def test_show_turn_player_a(self, input_value):
        move = self.theView.show_turn(["Player_A"])

        self.assertEqual(move, 1)

    @patch('builtins.input', side_effect=['9','2'])
    def test_show_turn_player_a(self, input_value):
        move = self.theView.show_turn(["Player_A"])

        self.assertEqual(move, 1)