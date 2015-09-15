#I want them to either get the message from secret.txt or put in their own message to decode


def main():

	f = open('secret.txt', 'r')
#		f.read()
	stuff = f.read()

#	note = getsecret(filename)

	decodednote = detransform(stuff)

	print(decodednote)

def detransform(filename):
 	

	numbers = filename.split()
	mystring = ""
#	print(numbers)
	for letter in numbers:
		mystring += chr(int(letter)) 


	return mystring


  
main()