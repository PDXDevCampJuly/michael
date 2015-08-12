#Prime
"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
   we can see that the 6th prime is 13. What is the 10 001st prime number?
"""

def isPrime(n, primes):
    if 0 not in [n%i for i in primes]:
        return True
    else:
        return False

def main(n):
    count = 2
    prime = [2,3,5,7]
    while count <= n:
        if isPrime(count, prime) == True:
            prime.append(count)
            count += 1
        else:
            count += 1

    print(len(prime))
    print(prime)
    makeFile(str(prime))


def makeFile(lprime):
    f = open('primes.txt','w')
    f.write(lprime)
    f.close

main(1000000)
