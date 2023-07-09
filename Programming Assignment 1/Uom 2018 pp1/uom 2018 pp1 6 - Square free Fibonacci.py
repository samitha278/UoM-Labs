#Solution by Bandara M.A.G.S.S

#Square free Fibonacci

def main():
    n = int(input().strip())
    
    nth_fibonacci = fibonacci(n)

    if issquare_free(nth_fibonacci):
        print("YES")
    else:
        print("NO")

def issquare_free(n):
    n_sqrt = int(n**0.5)
    primes_squares = [i*i for i in get_primes(n_sqrt)]

    if any(n%i==0 for i in primes_squares):
        return False

    return True
    

def get_primes(n):
    prime_seive = [True]*(n+1)
    prime_seive[0]=prime_seive[1] = False

    for i in range(2,int(n**0.5)+1):
        if prime_seive[i]:
            for j in range(i*i,n+1,i):
                prime_seive[j]=False

    primes = [i for i in range(len(prime_seive)) if prime_seive[i]]

    return primes

def fibonacci(n):
    a,b = 0,1

    temp = n
    while n!=0:
        a,b=b,a+b

        n-=1

    return a
         
main()
