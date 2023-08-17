def main():

    try:
        with open(input().strip()) as file:
            X = file.readline().rstrip()
    except:
        return -1

    
    Ns = getNs(X)

    sumProductNums = [N for N in Ns if isSumProduct(N)]

    if len(sumProductNums)==0:
        print(none)
    else:
        for num in sumProductNums:
            print(num,end = " ")
        print()





def isSumProduct(N):
    
    if len(N)==1:
        return N=='1'

    sumDigits = sum(map(int,N))

    productDigits = 1
    for digit in N:
        productDigits *= int(digit)

    sumProduct = sumDigits * productDigits

    if sumProduct==int(N):
        return True

    return False
    
    


    


def getNs(X):
    l = len(X)

    Ns = list(set(X))

    for i in range(2,l):

        for j in range(l-i+1):
            Ns.append(X[j:j+i])

    Ns.append(X)

    return Ns

#print(getNs('123456789'))








main()











    




    
