#Open File
def openFile(secretFile):
    openedFile = open(secretFile)
    readFile = openedFile.read()
    return(readFile)

#Transform String
def detransformStr(openedFile):
    #Define variables
    word = ""
    noSpaces = ""
    #Convert ASCE into letters
    for i in openedFile:
        if i == " ":
            i=""
            noSpaces += chr(int(word))
            word = ""
        #Save each character into a word
        word += i
    return(noSpaces)

#Decoder Main
def mainDecoder(stringName):
    unscrambledStr = detransformStr(openFile(stringName))
    print(unscrambledStr)

mainDecoder('secret.txt')
