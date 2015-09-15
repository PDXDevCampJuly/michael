#Ask for imput and put that imput into a funtion
#Encoder will look up the letter?(Maybe word?) in a dict and put out the matching thing in a file(???????)
import random, string
def main(message = None):
	if message == None:
		message = input("What do you want to write? ")

	transformin = transform(message)

#	makesecret(transformin)

def randomnumbers():
	number = '012345689'
	id = []
	for i in range(2):
		id += random.choice(number)

	return id

#def lengthnumbers


def transform(message):
	mystring = []
	for letter in message:
		mystring += str(ord(letter))



	s = mystring
	len(s)

	mergedlist = mystring + randomnumbers + len(s)

	print(mergedlist)

#	print(mystring,len(s),randomnumbers())

	return mystring


#def makesecret(secret):

#	with open('secret.txt', 'w') as f:
#		f.write(secret)

