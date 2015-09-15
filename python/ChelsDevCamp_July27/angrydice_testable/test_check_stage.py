__author__ = 'Chelsea'

import unittest
from angry_dice import Angry_dice


class CheckStageTest(unittest.TestCase):
    """Tests if current stage changes if given different die values"""

    def setUp(self):
        self.angry_game = Angry_dice()

    def tearDown(self):
        del self.angry_game

    #Both dies are equal and both are in stage one goals
    def test_stage_one_both_dice_equal(self):
        self.angry_game.die_a.currentValue = '1'
        self.angry_game.die_b.currentValue = '1'

        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 1)

    #One is in stage one goals and one is not
    def test_stage_one_with_one_and_three(self):
        self.angry_game.die_a.currentValue = '1'
        self.angry_game.die_b.currentValue = '3'

        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 1)

    #Both are in stage goals and they are not equal
    def test_stage_one_with_two_and_one(self):
        self.angry_game.die_a.currentValue = '2'
        self.angry_game.die_b.currentValue = '1'

        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 2)

    #Both are in stage goals and they are not equal but reverse
    def test_stage_one_with_one_and_two(self):
        self.angry_game.die_a.currentValue = '1'
        self.angry_game.die_b.currentValue = '2'

        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 2)

#Part two

    #Both dies are equal and both are in stage goals
    def test_stage_two_both_dice_four_ANGRY(self):
        self.angry_game.current_stage = 2
        self.angry_game.die_a.currentValue = '4'
        self.angry_game.die_b.currentValue = '4'

        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 2)

    #One is in stage goals and one is not
    def test_stage_two_with_one_and_three(self):
        self.angry_game.current_stage = 2
        self.angry_game.die_a.currentValue = '1'
        self.angry_game.die_b.currentValue = 'ANGRY'

        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 2)

    #Both are in stage goals and they are not equal
    def test_stage_two_with_four_and_one(self):
        self.angry_game.current_stage = 2
        self.angry_game.die_a.currentValue = '4'
        self.angry_game.die_b.currentValue = 'ANGRY'

        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 3)

    #Both are in stage goals and they are not equal but reverse
    def test_stage_two_with_one_and_four(self):
        self.angry_game.current_stage = 2
        self.angry_game.die_a.currentValue = '4'
        self.angry_game.die_b.currentValue = 'ANGRY'

        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 3)

#Part three

    #Both dies are equal and both are in stage goals
    def test_stage_three_die_six_six(self):
        self.angry_game.current_stage = 3
        self.angry_game.die_a.currentValue = '6'
        self.angry_game.die_b.currentValue = '6'

        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 3)

    #One is in stage goals and one is not
    def test_stage_three_with_five_and_one(self):
        self.angry_game.current_stage = 3
        self.angry_game.die_a.currentValue = '5'
        self.angry_game.die_b.currentValue = '1'

        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 3)

    #Both are in stage goals and they are not equal
    def test_stage_three_with_five_and_six(self):
        self.angry_game.current_stage = 3
        self.angry_game.die_a.currentValue = '5'
        self.angry_game.die_b.currentValue = '6'

        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 4)

    #Both are in stage goals and they are not equal but reverse
    def test_stage_three_with_fix_and_five(self):
        self.angry_game.current_stage = 3
        self.angry_game.die_a.currentValue = '6'
        self.angry_game.die_b.currentValue = '5'

        self.angry_game.check_stage()

        self.assertEqual(self.angry_game.current_stage, 4)


if __name__ == '__main__':
    unittest.main()
