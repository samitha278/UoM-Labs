#Solution by Bandara M.A.G.S.S

#Prime sieve


def main():
    while True:
        try:
            lim = int(input())
            break
        except ValueError:
            continue
        
    grid = create_grid(lim)

    print_primes(grid)

    return 0


def create_prime_sieve(n):
    prime_sieve = [True] * (n + 1)
    prime_sieve[0] = prime_sieve[1] = False

    sqrt = int(n ** 0.5) + 1
    for i in range(2, sqrt):
        if prime_sieve[i]:
            for j in range(i * i, n + 1, i):
                prime_sieve[j] = False

    return prime_sieve



def print_primes(prime_sieve):
    primes = [i for i, is_prime in enumerate(prime_sieve) if is_prime]
    print(' '.join(map(str, primes)))



def create_grid(n):
    grid = {i:"O" for i in range(2,n+1)}
    
    grid[1] = "X"

    for i in range(2,n+1):
        if grid[i] == "O":
            for m in range(i+i,n+1,i):
                if grid[m] == "O":
                    grid[m]="X"
    return grid



def print_primes(dic):
    for i in dic:
        if dic[i]=="O":
            print(i,end=" ")
    print()

    return 0


#driver code
if __name__ == '__main__':
    main()
