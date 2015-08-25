__author__ = 'Chelsea | Michael'

import unittest
from Conect4_View import View
from unittest.mock import patch
from io import StringIO


class TestViewShowBoard(unittest.TestCase):
    """make sure it prints an empty list"""

    def setUp(self):
        """Inits empty grid for testing"""
        self.theView = View()

    def tearDown(self):
        """ Closes the view """
        del self.theView

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_the_board(self, mock_stdout):
        """visually represent the grid as a connect 4 game """
        # first_row = "  1   2   3   4   5   6   7"
        currentBoard =\
            "                    "\
            "                    "\
            "                    "\
            "                    "\
            "                    "\
            "                    "\
            "--------------------"\
            "1  2  3  4  5  6  7 \n"

        self.theView.show_board([[" "] * 6 for x in range(7)])

        self.assertEqual(mock_stdout.getvalue(), currentBoard)

    @patch('sys.stdout', new_callable=StringIO)
    def show_one_row_in_board(self, mock_stdout):
        pass

    #def test_show_the_board(self):
     #  """ visually represent the grid as a connect 4 game """
     #  self.theView.show_board()
