#Solution by Bandara M.A.G.S.S

#Product of Primes

def main():
    '''main function'''
    
    num = get_int()             #call get_int() function

    p_fact = prime_fact(num)    #call prime_fact function

    print_dict(p_fact)          #call print_dict() function 

    return 0


def get_int():
    '''get integer from user'''
    while True:
        try:
            num = int(input())
        except:
            continue
        else:
            break
    return num
    

def prime_fact(n):
    '''return prime factorization given number as dictionary'''
    pf_dict = {}       #empty dictionary

    temp = n
    for i in prime_num(n):      #get prime numbers till given number
        if temp==1:
            break
        while temp%i==0:        #run untill temp not divides from i
            try:
                pf_dict[i]+=1
            except:
                pf_dict[i]=1
            temp //= i          #update temp 

    return pf_dict              #return dictionary

def prime_num(n):
    '''yield prime numbers till given number'''
    for i in range(2,n):
        if isPrime(i):          #check number is prime number
            yield i

def isPrime(n):
    '''check number is prime number or not if True otherwise False'''
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
def print_dict(dict):
    '''print prime factorization'''
    alist = list(dict.keys())
    str_out = ""
    for i in alist[:-1]:
        if dict[i] == 1:        #check if dict[i]==1
            str_out += str(i)
        else:
            str_out += str(i)+"^"+str(dict[i])
        str_out+=" X "
    else:
        x = alist[-1]
        if dict[x]==1:
            str_out+=str(x)
        else:
            str_out += str(x)+"^"+str(dict[x]) 

    print(str_out)               #print prime factorization
    return 0


#driver code
if __name__ == '__main__':
    main()











        
