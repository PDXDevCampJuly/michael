# this is a madlib program
#############################

# declaring variables
prompt = " >>> "
space = " "

# def madLib(input):
#   article += text + theInput
#   return article

article = "Pizza was invented by a "
theInput = input("Please type an 'abjective'" + prompt)
article += theInput

theInput = input("Please type a 'nationality'" + prompt)
article += space + theInput

article += " chef named "
theInput = input("Please type a 'person's name'" + prompt)
article += theInput

article += ". To make pizza, you need to take a lump of "
theInput = input("Please type a 'noun'" + prompt)
article += theInput

article += ", and make a thin, round "
theInput = input("Please type a 'adjective'" + prompt)
article += theInput

theInput = input("Please type a 'noun'" + prompt)
article += space + theInput

article += ". Then you cover it with "
theInput = input("Please type a 'noun'" + prompt)
article += theInput

article += " sauce,"
theInput = input("Please type an 'adjective'" + prompt)
article += theInput

article += " cheese, and fresh "
theInput = input("Please type a 'plural noun'" + prompt)
article += theInput

article += ". Next you have to bake it in a very hot "
theInput = input("Please type a 'noun'" + prompt)
article += theInput

article += ". When it is done, cut it into "
theInput = input("Please type a 'number'" + prompt)
article += theInput

theInput = input("Please type the plural form of a 'shape'" + prompt)
article += space + theInput

article += ". Some kids like "
theInput = input("Please type a kind of 'food'" + prompt)
article += theInput

article += " pizza the best but my favorite is "
theInput = input("Please type another type of 'food'" + prompt)
article += theInput

article += " pizza. If I could, I would eat pizza "
theInput = input("Please type a 'number'" + prompt)
article += theInput + " times a day! THE END"

print(article)








