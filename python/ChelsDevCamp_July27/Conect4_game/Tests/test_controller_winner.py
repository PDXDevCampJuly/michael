__author__ = 'Chelsea'

import unittest
from unittest.mock import patch
from io import StringIO

class check_if_winner_wins(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)

    def setUp(self):
        """Inits empty grid for testing"""
        self.controller = Controller()

    def tearDown(self):
        """ Closes the view """
        del self.controller

    def test_if_winner(self, ):

        board = [
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 2 + ["\u25CF"] * 4,
        [" "] * 6
        ]

        winner_print = "Yay! Player_a won! (^-^)"

        four_in_a_row = self.conroller.check_winner(1)
        self.assertEqual(winner_print, mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
