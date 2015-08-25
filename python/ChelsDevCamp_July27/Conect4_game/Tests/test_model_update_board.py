__author__ = 'Chelsea | Michael'

import unittest
from Conect4_Model import Model
from unittest.mock import patch

class TestModelUpdateBoard(unittest.TestCase):

    def setUp(self):
        """ Init's current player and players"""
        self.model = Model()

    def tearDown(self):
        """ Closes the model """
        del self.model

    def test_userinput_changes_board(self):

        self.model.update_board(5)

        mock_board = [
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 5 + ["\u25CF"],
        [" "] * 6
        ]

        self.assertEqual(self.model.grid, mock_board, "Column did not update")

    def test_userinput_changes_board(self):

        self.model.grid = [
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        ["\u25CF"] * 6,
        [" "] * 6
        ]

        column_full = self.model.update_board(5)


        self.assertTrue(column_full, "Board said column was not full")

    def test_userinput_changes_board(self):

        self.model.grid = [
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 3 + ["\u25CF"] * 3,
        [" "] * 6
        ]

        column_full = self.model.update_board(5)

        mock_board = [
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 6,
        [" "] * 2 + ["\u25CF"] * 4,
        [" "] * 6
        ]

        self.assertFalse(column_full, "Board said column was full")
        self.assertEqual(self.model.grid, mock_board, "Column did not update")



if __name__ == '__main__':
    unittest.main()
