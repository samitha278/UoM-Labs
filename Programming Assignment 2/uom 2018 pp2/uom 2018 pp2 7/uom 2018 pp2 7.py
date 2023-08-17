def main():

    integers = readFile(input().strip())
    if integers is None:return -1

    
    
    pSeive = getPrimeSeive(max(integers))

    pmFactors = [getPrimeFactors(pSeive,n) for n in integers]
    
    if writer("output.txt",pmFactors)==-1:return -1


def writer(outFile,output):
    try:
        with open(outFile,"w") as file:
            for line in output:
                print(line)
                file.write(str(line)+"\n")
    except Exception as e:
        print(e)
        return -1
    return 0
    

def getPrimeFactors(pSeive,n):

    pmFactors = [i for i in range(n) if pSeive[i] and n%i==0]

    return pmFactors



def getPrimeSeive(n):
    seive = [True]*(n+1)
    seive[0]=seive[1]=False

    pmDigits = [2,3,5,7]
    
    for i in pmDigits:
        for j in range(i*i,n+1,i):
            if seive[j]:
                seive[j]=False
                
    for i in range(11,int(n**0.5)+1):
        for j in range(i,n+1,i):
            if seive[j]:
                seive[j]=False
                
    return seive
    

def readFile(inpFile):
    try:
        with open(inpFile) as file:
            integer = list(map(int,(line.rstrip() for line in file)))

    except Exception as e:
        print(e)
        return

    return integer











main()
