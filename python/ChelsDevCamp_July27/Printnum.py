#Asking for the range of what numbers they want to print
firstnum = int(input("Enter a number: "))
secondnum = int(input("Enter a higher number: "))


def main():
	f = open('printnumbers.txt', 'w')
#For the number in the range they gave add one
	for num in range(firstnum,secondnum + 1):

		if num > 1:
			for i in range(2,num):
				if (num % i) == 0:
					break

			else:
				f.write(str(num) + "\n")

	f.close()