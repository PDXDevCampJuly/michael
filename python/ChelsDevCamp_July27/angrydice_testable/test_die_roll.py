__author__ = 'Chelsea'

import unittest
from die_Game_Aug10.Die_two_point_whoa import Die

class DieRollTest(unittest.TestCase):
    """Test functionality of the die class roll function"""

    def setUp(self):

        self.possable_values = [1,2,3,"Green","Blue","Yellow"]
        self.new_die = Die(self.possable_values)
        #print(self.shortDescription())

    def tearDown(self):
        #print("Just ran test")
        #print(self._testMethodName)
        pass


    def test_roll_once(self):
        """Roll the die once and ensure the returning value is in possibleValues"""

        self.assertIn(self.new_die.roll(), self.possable_values,"Rolled value was not in possibleValues of Die")

    def test_rolled_value_changes(self):
        """Roll the die a number of times and make sure it changes value"""

        holding_value = self.new_die.roll()
        for i in range(10):
            if self.new_die.roll() != holding_value:
                #print("Rolled die Value {} is different than holding Value {}"
                #    .format(self.new_die.currentValue, holding_value))
                self.assertTrue(True)
                return

        self.assertTrue(False, "Die value did not change from Holding Value for 10 rolls")

    def test_currentValue_is_updated_to_rolled_value(self):
        """Make sure that the Die's current value in updated to match what was rolled"""
        #
        # self.new_die_currentValue = 5
        #
        # self.assertEqual( self.new_die.roll(), self.new_die_currentValue,
        #                      "Current Values was not different from rolled")
        pass


if __name__ == '__main__':
    unittest.main()
