# prime numbers to x range
# ****************************

from sys import argv
from math import sqrt
from math import ceil

# take input from user, convert to int
capture = argv[1:]
userRange = int(capture[0])

def runTest(userRange):
  primes_list = [2]

  # the range skips all evens
  for n in range(3, userRange, 2):
    if squareRoot(n):
      primes_list.append(n)
  # print(primes_list)
  print("Final count:", len(primes_list))
  makeFile(primes_list)

# make square root rounded-up for n
def squareRoot(n):
  # num = n, ":", ceil(sqrt(n))
  numSqrt = ceil(sqrt(n))
  # print(num)
  return rangeSqrt(n, numSqrt)

# take the square root and find range up to the sqrt
def rangeSqrt(n, numSqrt):
  # print("rangeSqrt: ", n)
  testRange = list(range(2, numSqrt + 1))
  # print(testRange)
  return finalTest(n, testRange)

# run modulus test for the sqrt range
def finalTest(n, testRange):
  final_list = [n % x for x in testRange]
  return 0 not in final_list

# 0 not in [n % x for x in range(2, floor(sqrt(n)), 2)]

# write to an external file
def makeFile(list):
  # open, write, close file
  with open("primes.txt", 'w') as f:
    #   f.write("%s\n" % item)
    f.write(str(list))
  print("Transfer complete.")

runTest(userRange)

