import sys


def isPrime(num):
    if(num==2):
        return True
    else:
        for i in range(2,num):

            if(num%i==0):
                return False
            return True
        


def prime_10(n):
    length = n
    primeNumbers = []
    n=2

    while(len(primeNumbers)<=length):
        if(isPrime(n) == True):
            primeNumbers.append(n)
        n+= 1
    return primeNumbers


print(prime_10(int(sys.argv[0])))

