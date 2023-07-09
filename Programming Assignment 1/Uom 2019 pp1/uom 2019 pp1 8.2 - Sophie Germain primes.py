#Solution by Bandara M.A.G.S.S

#Sophie Germain primes

def main():
    p = int(input().strip())
    q = int(input().strip())

    sum_sophie_primes = sum(i for i in range(p,q+1) if is_sophie_prime(i))

    print(sum_sophie_primes)

    

def is_sophie_prime(n):
    x = 2*n+1
    if isPrime(n) and isPrime(x):
        return True
    else:
        return False

def isPrime(n):
    if n<=0 or n==1:
        return False
    elif n==2 or n==3 or n==5 or n==7:
        return True
    elif n%2==0 or n%3==0 or n%5==0 or n%7==0:
        return False
    for i in range(11,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True


main()


