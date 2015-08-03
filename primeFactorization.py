# "Prime Factorization" is finding which prime numbers multiply together to make the original number

# primes_list = [2, 3, 5, ...]
# n = integer to factor
# remainder = difference between n / prime in primes_list
# factor_list = answer to the algorithm

# >>>---------------------------------------------->

from sys import argv
from collections import Counter

filename = "primes.txt"

n = int(argv[1])

# retrieve the primes.txt file
with open(filename, "r") as f:
  primes_list = eval(f.read())

# alternate method reading line-by-line
# with open("primes.txt") as f:
#   primes = f.read().split('\n')[:-1] # ignores last line of the file

# make factors list
def factorize(n, primes_list):
  factors_list = []

  while n < 2:
    n = int(input("> Input integer greater than 1: "))

  while n > 1:
    for prime in primes_list:
      if n % prime == 0:
        n = n / prime
        factors_list.append(prime)
  print(factors_list)
  print(Counter(factors_list))

  # concat =

factorize(n, primes_list)

# group multiples to signify "power of"
# print "prime factors of %d are: " % target
"""
strs = []
for factor in factorList:
    strs.append(str(factor))
# strs = [str(factor) for factor in factorList]
print("{} =".format(target), " * ".join(strs))

# format somewhat more nicely with Counters
factors = Counter(factorList)
output = ["{}^{}".format(x, factors[x]) if factors[x] > 1 else str(x) for x in sorted(list(factors.keys()))]
print('{} ='.format(target), ' * '.join(output))
"""





