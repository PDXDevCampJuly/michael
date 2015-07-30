# prime numbers to x range
# ****************************

from sys import argv
from math import sqrt
from math import ceil

# take input from user, convert to int
capture = argv[1:]
userRange = int(capture[0])

def runTest(userRange):
  primes_list = []

  for n in range(1, userRange):
    if even(n) == "Pass":
      if squareRoot(n) == "Pass":
        primes_list.append(n)
  # print(primes_list)
  print("Final count:", len(primes_list))

  makeFile(primes_list)

def even(n):
  if n % 2 == 0 or n == 2:
    # print(n)
    return "Fail"
  else:
    # print(n)
    return "Pass"

# make square root rounded-up for n
def squareRoot(n):
  num = n, ":", ceil(sqrt(n))
  numSqrt = ceil(sqrt(n))
  # print(num)
  return rangeSqrt(n, numSqrt)

# take the square root and find range up to the sqrt
def rangeSqrt(n, numSqrt):
  # print("rangeSqrt: ", n)
  testRange = []
  for i in range(2, numSqrt + 1):
    testRange.append(i)
  # print(testRange)
  return finalTest(n, testRange)

# run modulus test for the sqrt range
def finalTest(n, testRange):
  final_list = []
  for num in testRange:
    if n % num == 0:
      final_list.append("Fail")
    else:
      final_list.append("Pass")
  if not "Fail" in final_list:
    return "Pass"

# write to an external file
def makeFile(list):
  # open, write, close file
  with open("primes.txt", 'w') as f:
    f.write(list)
  print("Transfer complete.")

runTest(userRange)

