#Palindrome
"""A palindromic number reads the same both ways. The largest palindrome
   made from the product of two 2-digit numbers is 9009 = 91 × 99.
   Find the largest palindrome made from the product of two 3-digit numbers.
"""
s="words"

#Return palindrome
def getPalindrome(number):
    reverseNum = str(number)[::-1]
    return reverseNum

def main():
    num1 = 999
    num2 = 999
    bigPal = 0

    for i in range(num1,100,-1):
        if i**2 < bigPal:
            break

        for j in range(num2, 100, -1):
            number = i*j
            if number < bigPal:
                break
            elif number == int(getPalindrome(number)):
                bigPal = number

    print(bigPal)


main()
