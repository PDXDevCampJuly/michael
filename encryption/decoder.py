# decoder
# this decoder will deconstruct the encoder module
##################################################

from sys import argv

# make a class main to get the encoder module
class Decoder():

  def __init__(self, fileName = "secret.txt"):
    self.fileName = fileName
    self.encodedString = self.getSecret()
    self.detransform()

  # make a function to "detransform" a string
  def detransform(self):
    messageList = []
    string = self.encodedString.split()
    for each_number in string:
      messageList.append(chr(int(each_number)))
    print(''.join(messageList))

  # make a function to get the secret message from the imported file
  def getSecret(self):

    with open(self.fileName, "r") as f:
      string = f.read()

    return string

if __name__ == '__main__':
  my_decoder = Decoder(*argv[1:])

