__author__ = 'Chelsea'

import unittest
from angry_dice import Angry_dice
from unittest.mock import patch
from io import StringIO


class CheckAngryTest(unittest.TestCase):
    """Test if current stage changes if both die values are 'ANGRY' """

    def setUp(self):
        self.angry_game = Angry_dice()

    def tearDown(self):
        del self.angry_game

    @patch('sys.stdout', new_callable=StringIO)
    def test_check_stage_one_angry_angry(self, mock_stdout):
        self.angry_game.die_a.currentValue = 'ANGRY'
        self.angry_game.die_b.currentValue = 'ANGRY'
        self.angry_game.current_stage = 1
        angry_text = "You're very angry, you need to calm down\n"

        self.angry_game.check_angry()

        self.assertEqual(mock_stdout.getvalue(), angry_text)
        self.assertEqual(self.angry_game.current_stage, 1)

    def test_check_stage_one_angry_two(self):
        self.angry_game.die_a.currentValue = 'ANGRY'
        self.angry_game.die_b.currentValue = '2'
        self.angry_game.current_stage = 1

        self.angry_game.check_angry()

        self.assertEqual(self.angry_game.current_stage, 1)

    def test_check_stage_one_angry_five_two(self):
        self.angry_game.die_a.currentValue = '5'
        self.angry_game.die_b.currentValue = '2'
        self.angry_game.current_stage = 1

        self.angry_game.check_angry()

        self.assertEqual(self.angry_game.current_stage, 1)

    # Part two
    def test_check_stage_two_angry_angry(self):
        self.angry_game.die_a.currentValue = 'ANGRY'
        self.angry_game.die_b.currentValue = 'ANGRY'
        self.angry_game.current_stage = 2

        self.angry_game.check_angry()

        self.assertEqual(self.angry_game.current_stage, 1)

    def test_check_stage_two_angry_two(self):
        self.angry_game.die_a.currentValue = 'ANGRY'
        self.angry_game.die_b.currentValue = '2'
        self.angry_game.current_stage = 2

        self.angry_game.check_angry()

        self.assertEqual(self.angry_game.current_stage, 2)

    def test_check_stage_two_angry_five_two(self):
        self.angry_game.die_a.currentValue = '5'
        self.angry_game.die_b.currentValue = '2'
        self.angry_game.current_stage = 2

        self.angry_game.check_angry()

        self.assertEqual(self.angry_game.current_stage, 2)

    # Part three

    def test_check_stage_three_angry_angry(self):
        self.angry_game.die_a.currentValue = 'ANGRY'
        self.angry_game.die_b.currentValue = 'ANGRY'
        self.angry_game.current_stage = 3

        self.angry_game.check_angry()

        self.assertEqual(self.angry_game.current_stage, 1)

    def test_check_stage_three_angry_two(self):
        self.angry_game.die_a.currentValue = 'ANGRY'
        self.angry_game.die_b.currentValue = '2'
        self.angry_game.current_stage = 3

        self.angry_game.check_angry()

        self.assertEqual(self.angry_game.current_stage, 3)

    def test_check_stage_three_angry_five_two(self):
        self.angry_game.die_a.currentValue = '5'
        self.angry_game.die_b.currentValue = '2'
        self.angry_game.current_stage = 3

        self.angry_game.check_angry()

        self.assertEqual(self.angry_game.current_stage, 3)


if __name__ == '__main__':
    unittest.main()
