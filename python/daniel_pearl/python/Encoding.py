"""
1. Take a string, feed through encoder, output scramble txt file
    a. main(message=None):filename
    b. transform(str):str
    c. makeSecret(str, file="secret.txt":filename

2. Take a file, feed into decoder, print string
    a. main(filename="secret.txt")
    b. de-transform(str):str
    c. getSecret(file="secret.txt"):str
"""

#Encoder Main
def mainEncoder(string=None):
    if string == None:
        string = input("Please enter your message: ")
    #Catch string from transformStr function
    scrambledStr = transformStr(string)
    makeSecret(scrambledStr)

#Transform String
def transformStr(string):
    ordStr = ""
    #Convert letters to ASCE
    for i in string:
        ordStr += str(ord(i)) + " "
    return ordStr

#Convert scrambled string to File
def makeSecret(scrambledStr):
    f = open('secret.txt','w')
    f.write(scrambledStr)
    f.close

x="something here"
mainEncoder(x)
