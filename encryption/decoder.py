# decoder
# this decoder will deconstruct the encoder module
##################################################

from sys import argv

# make a class main to get the encoder module
class Decoder():

  def __init__(self, fileName = "secret.txt"):
    self.fileName = fileName
    self.getSecret()
    self.level()

  # determine the level to decode
  def level(self):
    string = self.encodedString.split()
    if len(string[0]) > 3:
      self.detransform_2(string)
    else:
      self.detransform_1(string)

  # make a function to "detransform" a string
  def detransform_1(self, string):
    messageList = []
    for each_number in string:
      messageList.append(chr(int(each_number)))
    print(''.join(messageList))

  def detransform_2(self, string):
    messageList = []
    for each_number in string:
      part1 = each_number[3:]
      part2 = part1[:-2]
      messageList.append(chr(int(part2)))
    print(''.join(messageList))

  # make a function to get the secret message from the imported file
  def getSecret(self):
    with open(self.fileName, "r") as f:
      self.encodedString = f.read()

if __name__ == '__main__':
  my_decoder = Decoder(*argv[1:])

