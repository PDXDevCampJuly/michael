__author__ = 'mw'

import unittest
from angry_dice import AngryDice


class TestAngryDiceStage2(unittest.TestCase):

    def setUp(self):
        """ Initializes the die for the following testing functions """

        self.game = AngryDice()
        # print(self.shortDescription())

    def tearDown(self):
        """ delete the instance of game after running tests """
        del self.game

    def test_stage2_aAngry_b4(self):
        """ [1, 2] stage becomes 2 """
        self.game.stage = 2
        self.game.stage_2("ANGRY", "4")
        self.assertEqual(3, self.game.stage, "[Angry, 4], changes to stage 3")
        self.assertIn("Stage 2 completed", self.game.outcome, "now stage 3")

    def test_stage2_aAngry_b1(self):
        """ [1, 2] stage stays 1 """
        self.game.stage = 2
        self.game.stage_2("ANGRY", "1")
        self.assertNotEqual(3, self.game.stage, "[Angry, 1], stays at stage 2")
        self.assertNotIn("Stage 2 completed", self.game.outcome,
                         "stay stage 2")


    def test_stage2_a4_bAngry(self):
        """ [2, 1] stage becomes 2 """
        self.game.stage = 2
        self.game.stage_2("4", "ANGRY")
        self.assertEqual(3, self.game.stage, "[4, Angry], changes to stage 3")
        self.assertIn("Stage 2 completed", self.game.outcome, "now stage 3")

    def test_stage2_a1_b1(self):
        """ [3, 3] stage stays 1 """
        self.game.stage = 2
        self.game.stage_2("1", "1")
        self.assertNotEqual(3, self.game.stage, "[1, 1], stays at stage 2")
        self.assertNotIn("Stage 2 completed", self.game.outcome,
                         "stay stage 2")


if __name__ == '__main__':
    unittest.main()
