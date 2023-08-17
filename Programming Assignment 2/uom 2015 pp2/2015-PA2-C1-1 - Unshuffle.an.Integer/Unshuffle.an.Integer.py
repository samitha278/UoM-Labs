def main():

    q = readFile(input().strip())
    if q is None:return -1


    k = getK(q)
    possible_n = removeK(k,q)

    smallest_n = getSmallest(possible_n)
    
    output = smallest_n

    if writer("output.txt",output)==-1:return -1






def writer(outFile,output):
    try:
        with open(outFile,"w") as file:
            file.write(output)
            print(output)
                

    except:
        return -1

def getSmallest(n):

    nlst = list(n)
    nlst.sort()

    return "".join(nlst)

    
    

def removeK(k,q):

    klst = list(str(k))
    qlst = list(q)

    for i in klst:
        qlst.remove(i)

    return "".join(qlst)

    


    
def getK(q):

    l = len(q)
    print(l)
    
    bench = [12,103,1004,10005,100006]

    
    for i in range(5):
        if bench[i]>l:
            k = l-(i+1)
            break

    return k


    

#print(getK(123456789810))


    




def readFile(inpFile):
    try:
        with open(inpFile) as file:
            q = file.read()
            
            if ('0' in q) or (not len(q)<1000000):
                raise Exception

    except Exception as e:
        print(e)
        return
    return q













if __name__=="__main__":
    main()
    
