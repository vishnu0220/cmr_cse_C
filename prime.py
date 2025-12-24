import math as m
n = int(input())

# Method 1
def isPrime1(n):
    isPrime = True
    cnt = 0
    for i in range(2, n):
        cnt += 1
        if n % i == 0:
            isPrime = False
            print("Not a prime")
            break
    if isPrime == True:
        print("Prime")
    print(cnt, " iterations done in Method 1")

# Method 2
def isPrime2(n):
    isPrime = True
    cnt = 0
    for i in range(2, (n//2+1)):
        cnt += 1
        if n % i == 0:
            isPrime = False
            print("Not a prime")
            break
    if isPrime == True:
        print("Prime")
    print(cnt, " iterations done in Method 2")

# Method 3
def isPrime3(n):
    isPrime = True
    cnt = 0
    for i in range(2, int(m.sqrt(n))+1):
        cnt += 1
        if n % i == 0:
            isPrime = False
            print("Not a prime")
            break
    if isPrime == True:
        print("Prime")
    print(cnt, " iterations done in Method 3")

isPrime1(n)
isPrime2(n)
isPrime3(n)