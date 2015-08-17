__author__ = 'mw'

import unittest
from dice_class import Die


class DieRollTest(unittest.TestCase):
    """ Test the functionality of the Dice_class roll function. """


    def setUp(self):
        """ Initializes the die for the following testing functions """

        self.possible_values = [1, 2, 3, 'dog', 'cat', 'hippo']
        self.new_die = Die(self.possible_values)

        print(self.shortDescription())


    def tearDown(self):
        """ Runs commands after each test """

        del self.possible_values
        del self.new_die
        print("Just ran test:")
        print(self._testMethodName)


    def test_roll_once(self):
        """ Roll the die once and ensure the returned value is in the list
        of possibleValues """

        self.assertIn(self.new_die.roll(), self.possible_values, "Rolled "
                        "value was not in possibleValues of Die.")


    def test_rolled_value_changes(self):
        """ Roll the die a number of times to make sure it changes value """

        holding_value = self.new_die.roll()
        for i in range(10):
            if self.new_die.roll() != holding_value:
                # print("Rolled Die value is {} different than holding_value
                #  {}".format(self.new_die.currentValue, holding_value))
                self.assertTrue(True)
                return

        self.assertTrue(False, "Die Value did not change from holding_value "
                        "for 10 rolls")


    def test_currentValue_is_updated_to_rolled_value(self):
        """ Make sure that the die's currentValue is updated to match what is rolled. """
        self.new_die.currentValue = 5
        self.assertEqual(self.new_die.roll(), self.new_die.currentValue,
                            "Current Value was not different from rolled")


if __name__ == '__main__':
    unittest.main()
