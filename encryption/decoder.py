# decoder
# this decoder will deconstruct the encoder module
##################################################

from sys import argv

# make a class main to get the encoder module
class Decoder():

  def __init__(self, fileName = "secret.txt"):
    self.fileName = fileName
    self.encodedString = self.getSecret()
    self.level()

  # determine the level to decode
  def level(self):
    string = self.encodedString.split()
    if len(string[0]) > 3:
      if len(string[0]) > 2:
        self.detransform_2()
    else:
      self.detransform_1()

  # make a function to "detransform" a string
  def detransform_1(self):
    messageList = []
    string = self.encodedString.split()
    for each_number in string:
      messageList.append(chr(int(each_number)))
    print(''.join(messageList))

  def detransform_2(self):
    messageList = []
    string = self.encodedString.split()
    for each_number in string:
      part1 = each_number[3:]
      part2 = part1[:-2]
      messageList.append(chr(int(part2)))
    print(''.join(messageList))

  # make a function to get the secret message from the imported file
  def getSecret(self):
    with open(self.fileName, "r") as f:
      string = f.read()
    return string

if __name__ == '__main__':
  my_decoder = Decoder(*argv[1:])

