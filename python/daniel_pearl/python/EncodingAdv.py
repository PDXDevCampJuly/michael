from random import randint

#Encoder Main
def mainEncoder(string=None):
    if string == None:
        string = input("Please enter your message: ")
    #Catch string from transformStr function
    scrambledStr = transformStr(string)
    makeSecret(scrambledStr)

#Transform string
def transformStr(string):
    ordStr = ""
    #Convert letters to ASCE
    for i in string:
        ordStr += str(len(str(ord(i)))) + str(randint(10,99)) + str(ord(i)) + str(randint(10,99)) + " "
    return ordStr

#Convert scrambled string to File
def makeSecret(scrambledStr):
    f = open('secret.txt','w')
    f.write(scrambledStr)
    f.close

x="This is a sentence"
mainEncoder(x)
