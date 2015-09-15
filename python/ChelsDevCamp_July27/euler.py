from sys import argv

maximum = int(argv[1])
primes = [2, 3, 5]

for n in range(7, maximum + 1, 6):
	is_prime = True
	for p in primes:
		if n % p == 0:
			is_prime = False
			break

	is is_prime:
				primes.append(n)

	if 0 not in [(n + 4) % p for p in primes]:
		primes.append(n + 4)

with open('primes.txt', 'w') as f:
	for p in primes:
		f.write(str(p)+'\n')

#f.write('\n'.join([str(p) for p in primes]))



##################
from sys import argv
from collection import Counter

target = int(argv[1])
with open("primes.txt") as f:
	primes = f.read().split('\n')[:-1]

	primes = [int(p) for p in primes]


factorList = []
remainder = target
for p in primes:
	while remainder % p == 0:
		factorList.append(p)
		remainder = remainder // p
	if remainder == 1:
		break
str = []
for factor in factorList:
	strs.append(str(factor))
print("{} =".format(x, factor[x]) if factor)

