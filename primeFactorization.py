# "Prime Factorization" is finding which prime numbers multiply together to make the original number

# primes_list = [2, 3, 5, ...]
# n = integer to factor
# remainder = difference between n / prime in primes_list
# factor_list = answer to the algorithm

# >>>---------------------------------------------->

from sys import argv
from collections import Counter

filename = "primes.txt"

capture = int(argv[1])
n = int(capture[0])

# retrieve the primes.txt file
with open(filename, "r") as f:
  primes_list = eval(f.read())

# make factors list
def factorize(n, primes_list):
  factors_list = []

  while n > 1:
    for prime in primes_list:
      if n % prime == 0:
        n = n / prime
        factors_list.append(prime)
  print(factors_list)
  print(Counter(factors_list))

factorize(n, primes_list)

# group multiples to signify "power of"






