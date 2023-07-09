#Solution by Bandara M.A.G.S.S

#Pisano period 

def main():
    n = int(input().strip())
    if not 1 < n < 10:
        return -1

    fibonaccis = get_fibonaccis(n)
    pi_period = pisano_period(n, fibonaccis)

    print(pi_period)


def pisano_period(n, fibos):
    for j in range(2, len(fibos)):
        if fibos[j] % n == 0 and fibos[j + 1] % n == 1:
            return j

    return -1


def get_fibonaccis(n):
    fibos = [0, 1]

    for i in range(2, n * 6):  # Pisano period for any n is at most 6n
        fibos.append((fibos[i - 1] + fibos[i - 2]) % n)

    return fibos


main()




def main():
    n = int(input().strip())
    if not 1<n<10:
        return -1

    fibonaccis = get_fibonaccis(50)

    pi_period = pisano_period(n,fibonaccis)

    print(pi_period)


def pisano_period(n,fibos):
    modulo_fibos = [i%n for i in fibos]

    for j in range(1,26):

        if j<17:
            repeats = [modulo_fibos[j*k:j*(k+1)] for k in range(3)]
        elif j<26:
            repeats = [modulo_fibos[j*k:j*(k+1)] for k in range(2)]

        if all(repeats[0]==repeats[i] for i in range(1,len(repeats))):
            return j
        
    
def get_fibonaccis(n):
    fibos = [0]*(n+1)
    fibos[0]=0
    fibos[1]=1

    for i in range(2,n+1):
        fibos[i] = fibos[i-1]+fibos[i-2]

    return fibos

#main()
    

    
