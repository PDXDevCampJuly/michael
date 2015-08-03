# encoder
# this encoder will construct a module for the decoder
######################################################

from sys import argv
from random import randint

# make a class main to begin the encoder program
class Encoder():

  def __init__(self, message = "", fileName = "secret.txt", level = 1):
    self.message = self.testInput(message)
    self.fileName = fileName
    self.transformLevel(int(level))
    self.makeFile()

  def testInput(self, message):
    # checks if the user already threw and arg for message
    # if message is an empty string ("no"t message), then ask for msg
    if not message:
      message = input("Input message: ")
    return message

  # determine the level to encode
  def transformLevel(self, level):
    if level == 1:
      self.level = 1
      self.transform_1()
    elif level == 2:
      self.level = 2
      self.transform_2()
    else:
      self.level = input("Input level 1 or 2: ")
      self.transformLevel(int(level))

  # make a function to transform a string level = 1
  def transform_1(self):
    messageList = []

    for each_letter in self.message:
      messageList.append(str(ord(each_letter)))
      string = ' '.join(messageList)
    print(messageList)
    self.encodedMessage = string

  # make a function to transform a string level = 2
  def transform_2(self):
    messageList = []

    for each_letter in self.message:
      toOrd = str(ord(each_letter))
      random1 = str(randint(10, 99))
      random2 = str(randint(10, 99))
      encoded = str(len(toOrd)) + random1 + toOrd + random2
      messageList.append(encoded)
      string = ' '.join(messageList)
    # print(messageList)
    self.encodedMessage = string

  # make a function to make a secret fileName
  def makeFile(self):
    # open, write, close file
    with open(self.fileName, 'w') as f:
      f.write(self.encodedMessage)
    print("Encryption complete.")

if __name__ == '__main__':
  my_encoder = Encoder(*argv[1:])

