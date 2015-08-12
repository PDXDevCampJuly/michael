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
            #Create slice depending on first number in string
            if word[0] == '2':
                noSpaces += chr(int(word[3:5]))
            else:
                noSpaces += chr(int(word[3:6]))
            word = ""
        #Save each character into a word
        word += i
    return(noSpaces)

#Decoder Main
def mainDecoder(stringName):
    unscrambledStr = detransformStr(openFile(stringName))
    print(unscrambledStr)

mainDecoder('secret.txt')
