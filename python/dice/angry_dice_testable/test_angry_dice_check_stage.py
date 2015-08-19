__author__ = 'mw'

import unittest
from angry_dice import AngryDice
from unittest.mock import patch


class TestAngryDiceCheckStage(unittest.TestCase):

    def setUp(self):
        """ Initializes the die for the following testing functions """
        self.game = AngryDice()
        # print(self.shortDescription())

    def tearDown(self):
        """ delete the instance of game after running tests """
        del self.game

    def test_check_stage_stage2_aAngry_bAngry(self):
        """ [Angry, Angry], does stage 2 change aAngry, bAngry """
        self.game.die_a.currentValue = "ANGRY"
        self.game.die_b.currentValue = "ANGRY"
        self.game.stage = 2
        self.game.check_stage()
        self.assertEqual(1, self.game.stage,
                            "[Angry, Angry], stage 2 changes to 1")
        self.assertIn("back to Stage 1", self.game.outcome, "reset to stage 1")

    def test_check_stage_stage3_aAngry_bAngry(self):
        """ [Angry, Angry], does stage 3 change aAngry, bAngry """
        self.game.die_a.currentValue = "ANGRY"
        self.game.die_b.currentValue = "ANGRY"
        self.game.stage = 3
        self.game.check_stage()
        self.assertEqual(1, self.game.stage,
                            "[Angry, Angry], stage 3 changes to 1")
        self.assertIn("back to Stage 1", self.game.outcome, "reset to stage 1")

    def test_check_stage_stage2_a1_bAngry(self):
        """ [Angry, 1], does stage 2 remain a1, bAngry """
        self.game.die_a.currentValue = "1"
        self.game.die_b.currentValue = "ANGRY"
        self.game.stage = 2
        self.game.check_stage()
        self.assertNotEqual(1, self.game.stage,
                            "[1, Angry], stage 2 still 2")
        self.assertNotIn("back to Stage 1", self.game.outcome,
                         "remain on Stage 2")


if __name__ == '__main__':
    unittest.main()
