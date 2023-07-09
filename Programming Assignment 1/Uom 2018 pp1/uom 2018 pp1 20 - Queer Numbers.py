#Solution by Bandara M.A.G.S.S

#Queer Numbers

def main():
    n1,n2 = get_ints()

    num_of_queers = find_queers(n1,n2)

    print(num_of_queers)


def find_queers(p,q):

    num_queers = len(list(i for i in range(p,q+1) if isQueer(i)))

    return num_queers
    
def isQueer(n):
    n_str = str(n)

    l = len(n_str)

    primes = []

    for i in range(l-1):
        num = int(n_str[i]+n_str[i+1])

        if not isPrime(num):
            return False
        else:
            if num in primes:
                return False
            else:
                primes.append(num)

    return True

def isPrime(n):
    if n==1 or n==0:
        return False
    if n==2:
        return True
    if n%2==0:
        return False

    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False

    return True
        
def get_ints():
    while True:
        try:
            inputs = list(map(int,input().strip().split()))
        except:
            print("invalid inputs")

        n1,n2 = inputs

        if 0<n1<n2:
            break

    return n1,n2


main()
