#Solution by Bandara M.A.G.S.S

#Palindromic primes


def main():
    ran = get_range()

    pal_sum = palindrom_sum(ran)

    print(pal_sum)

    return 0





def palindrom_sum(ran):
    p,q = ran
    
    pal_sum = 0

    for i in range(p,q+1):
        if isPalin(i):
            if isPrime(i) or isSqr(i):
                pal_sum +=i

    return pal_sum

def isPalin(n):
    n_str = str(n)

    l = len(n_str)
    if l == 1:
        return True
    elif l == 2:
        if n_str[0]==n_str[1]:
            return True
        else:
            return False
        
    if n_str[0]==n_str[-1]:
        return isPalin(int(n_str[1:-1]))
    else:
        return False
    

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def isSqr(n):
    sqr = n**0.5
    sqr_len = str(sqr)
    
    index = sqr_len.index(".")
    flo = int(sqr_len[index+1:])

    if flo==0:
        return True   
    return False

def get_range():
    while True:
        inp_str = input().strip()
        try:
            inp = list(map(int,inp_str.split()))
        except:
            continue
        else:
            l = len(inp)
            if l==2 and inp[0]<inp[1] and inp[0]>0:
                break
    return inp

if __name__=='__main__':
    main()
