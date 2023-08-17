def main():

    Ns = readFile(input().strip())
    if Ns is None: return -1
    print(Ns)

    results = [get_number_of_primes(N) for N in Ns]

    for result in results:
        print(result)


def get_number_of_primes(N):

    grid = [[0]*(N+1) for i in range(N+1)]

    
    count = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            grid[i][j] = val = gcd(i,j)

            if isPrime(val):
                count+=1

    return count      

    
    
            
            
def gcd(i,j):
    ifac = [k for k in range(1,i+1) if i%k==0] 
    jfac = [k for k in range(1,j+1) if j%k==0]

    diff = list(set(ifac).intersection(set(jfac)))

    return max(diff)


def isPrime(n):

    if n<=7:
        return n==2 or n==3 or n==5 or n==7

    if n%2==0 or n%3==0 or n%5==0 or n%7==0:
        return False

    for i in range(11,int(n**0.5)+1):
        if n%i==0:
            return False

    return True





    

def readFile(inpFile):
    try:
        with open(inpFile) as file:
            Ns = [int(line.rstrip()) for line in file]
    except Exception as e:
        print(e)
        return
    return Ns


main()
