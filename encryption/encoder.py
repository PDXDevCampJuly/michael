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
    self.level = self.transformLevel(int(level))
    self.encodedMessage = self.transform_1()
    self.makeFile()

  def testInput(self, message):
    # checks if the user already threw and arg for message
    # if message is an empty string ("no"t message), then ask for msg
    if not message:
      message = input("Input message: ")
    return message

  def transformLevel(self, level):
    if level == 1:
      self.transform_1()
    elif level == 2:
      self.transform_2()
    else:
      level = input("Input level 1 or 2: ")
      self.transformLevel(int(level))

  # make a function transform a string level = 1
  def transform_1(self):
    messageList = []
    for each_letter in self.message:
      messageList.append(str(ord(each_letter)))
      string = ' '.join(messageList)
    return string

  def transform_2(self):
    messageList = []
    newList = []
    lenList = []

    for each_letter in self.message:
      messageList.append(each_letter)
    lenMessageList = len(messageList)
    list1 = list(range(0, lenMessageList))
    list2 = list(range(0, lenMessageList))
    list3 = list(range(0, lenMessageList))
    list4 = list(range(0, lenMessageList))

    for each_item in list1:
      list1[each_item] = str(randint(10, 99))
    for each_item in list2:
      list2[each_item] = str(randint(10, 99))
    for each_item in list3:
      list3[each_item] = str(randint(10, 99))
    for each_item in list4:
      list4[each_item] = str(randint(10, 99))
    newList = [a + b + c + d + e for a, b, c, d, e in zip(list1, list2, messageList, list3, list4)]
    for each_item in newList:
      lenList.append(str(len(each_item)))
    finalList = [a + b for a, b in zip(lenList, newList)]

    print(messageList)
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(newList)
    print(lenList)
    print(finalList)

  # make a function to make a secret fileName
  def makeFile(self):
    # open, write, close file
    with open(self.fileName, 'w') as f:
      f.write(self.encodedMessage)
    print("Encryption complete.")

if __name__ == '__main__':
  my_encoder = Encoder(*argv[1:])

