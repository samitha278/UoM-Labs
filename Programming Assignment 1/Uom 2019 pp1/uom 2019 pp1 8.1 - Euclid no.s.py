#Solution by Bandara M.A.G.S.S

#Euclid nos

import math

def main():
    n = get_int()

    euclid_number = get_euclid_num(n)

    print(euclid_number)

    
def get_euclid_num(n):
    '''return nth euclid number'''
    
    n_primes = get_primes(n)
    euclid_number = math.prod(n_primes) + 1

    return euclid_number

'''def mul_nums(alist):
    #return product of all number in list
    p = 1
    for i in alist:
        p*=i

    return p'''

def get_primes(n):
    '''return list which contain first n prime numbers'''
    
    primes = []
    i = 2
    while len(primes)!=n:
        if isPrime(i):
            primes.append(i)

        i+=1
        

    return primes


def isPrime(n):
    '''check given number is prime number or not'''
    if n==2:
        return True
    if n<2 or n%2==0:
        return False

    isqr = int(n**0.5)

    #loop iterate odd numbers till square root of n
    for i in range(3,isqr+1,2):
        if n%i==0:
            return False
    return True


def get_int():
    '''get integer from user and return'''
    while True:
        n_str = input().strip()

        try:
            n = int(n_str)
        except:
            print("Invalid input")
            continue

        if n<=0:
            continue
        return n

main()
