import unittest
from dice_class import Die


class TestDiceClass(unittest.TestCase):

  def test_init(self):
    myDie = Die(["test1", "test2", "test3", "test4"])
    self.assertIn(str(myDie), ["test1", "test2", "test3", "test4"])

  def test_roll(self):
    pass

  def test_repr(self):
    pass

if __name__ == "__main__":
  unittest.main()
