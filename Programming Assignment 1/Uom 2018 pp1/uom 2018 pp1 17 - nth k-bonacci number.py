#Solution by Bandara M.A.G.S.S

#nth k-bonacci number

def main():
    k,n = list(map(int,input().strip().split()))
    if k<2 or k>100:return -1
    
    if n<1 or n>10000:return -1

    
    nth_kbo = kbonacci(k,n)
    print(nth_kbo)
    
def kbonacci(k,n):
    kbos = [0]*(n+1)

    for j in range(1,k+1):
        kbos[j]=1

    for i in range(k+1,n+1):
        kbos[i] = sum(kbos[i-k] for k in range(1,k+1))

    return kbos[n]

    
    
main()
