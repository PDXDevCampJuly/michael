__author__ = 'Chelsea'

import unittest
from unittest.mock import patch
from io import StringIO
from Conect4_Controller import Controller

class test_check_if_tie(unittest.TestCase):


    def setUp(self):
        """Inits empty grid for testing"""
        self.controller = Controller()

    def tearDown(self):
        """ Closes the controller """
        del self.controller
    @patch('sys.stdout', new_callable=StringIO)
    def test_if_tie(self, mock_stdout):

        mock_board = [
        ["\u25CF"] * 6,
        ["\u25CF"] * 6,
        ["\u25CF"] * 6,
        ["\u25CF"] * 6,
        ["\u25CF"] * 6,
        ["\u25CF"] * 6,
        ["\u25CF"] * 6,
        ]

        tie_print = "Yay! It's a tie! (^-^)"

        self.controller.check_tie()
        self.assertEqual(tie_print, mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()