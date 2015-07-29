# encoder
# this encoder will construct a module for the decoder
######################################################

from sys import argv

# make a class main to begin the encoder program
class Encoder():

  def __init__(self, message = "", fileName = "secret.txt"):
    self.message = self.testInput(message)
    self.fileName = fileName
    self.encodedMessage = self.transform()
    self.makeFile()

  def testInput(self, userInput):
    if not userInput:
      userInput = input("Input your secret message: ")
    return userInput

  # make a function transform a string
  def transform(self):
    messageList = []
    for each_letter in self.message:
      messageList.append(str(ord(each_letter)))
      string = ' '.join(messageList)
    return string

  # make a function to make a secret fileName
  def makeFile(self):
    # open, write, close file
    with open(self.fileName, 'w') as f:
      f.write(self.encodedMessage)

if __name__ == '__main__':
  my_encoder = Encoder(*argv[1:])

