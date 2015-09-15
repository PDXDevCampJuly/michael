__author__ = 'Chelsea'

import unittest
from unittest.mock import patch
from io import StringIO
from Conect4_Controller import Controller


class TestControllerCheckTie(unittest.TestCase):
    """ Check for controller for the situation of a a tie, full board """

    def setUp(self):
        """Inits empty grid for testing"""
        self.controller = Controller()

    def tearDown(self):
        """ Closes the controller """
        del self.controller

    @patch('sys.stdout', new_callable=StringIO)
    def test_if_tie_completely_full(self, mock_stdout):
        """ Check if board is completely full call show_tie and print that it's a tie """

        self.controller.board = [
        ["\u25CF"] * 6,
        ["\u25CF"] * 6,
        ["\u25CF"] * 6,
        ["\u25CF"] * 6,
        ["\u25CF"] * 6,
        ["\u25CF"] * 6,
        ["\u25CF"] * 6,
        ]

        tie_print = "Yay! It's a tie! (^-^)\n"

        self.controller.check_tie()
        self.assertEqual(tie_print, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_if_tie_partially_full(self, mock_stdout):
        """ Check if board is partially full call show_tie and print that it's a tie """

        self.controller.board = [
        [" "] * 3 + ["\u25CF"] * 3,
        ["\u25CF"] * 6,
        ["\u25CF"] * 6,
        ["\u25CF"] * 6,
        ["\u25CF"] * 6,
        ["\u25CF"] * 6,
        ["\u25CF"] * 6,
        ]

        tie_print = "Yay! It's a tie! (^-^)\n"

        self.controller.check_tie()
        self.assertNotEqual(tie_print, mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
