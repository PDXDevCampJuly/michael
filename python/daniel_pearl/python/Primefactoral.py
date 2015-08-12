#Prime Factorals
def getFactor(n, dlist):

    #Returns prime factors
    d = 2

    while n > 1:
        while n % d == 0:
            dlist.append(d)
            n /= d
        d += 1

        #60 = 2:2, 3:1, 5:1

    print (n)
    return dlist

def main(n):
    dictionary = {}
    plist=[]
    getFactor(n,plist)
    print(plist)


main(120)
