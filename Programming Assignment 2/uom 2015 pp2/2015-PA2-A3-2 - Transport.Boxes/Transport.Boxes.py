def main():
    data = readFile(input().strip())
    if data is None:return -1


    result = []
    for tup in data:
        n,k = tup
        result.append(getTrucks(n,k))


    if writer("result.txt",result)==-1:return -1

    




def writer(outFile,output):
    try:
        with open(outFile,"w") as file:
            for line in output:
                print(line)
                file.write(str(line)+"\n")
    except Exception as e:
        print()
        return -1



def getTrucks(n,k):
    
    if n<=k:
        return 1

    if n%2==0:
        fset = n//2
        return 2*getTrucks(fset,k)
    else:
        fset = (n//2)+1
        sset = n//2
        return getTrucks(fset,k)+getTrucks(sset,k)
    

    
#print(getTrucks(1024,5))
    



def readFile(inpFile):
    try:
        with open(inpFile) as file:
            lsts = [tuple(map(int,line.rstrip().split())) for  line in file]

    except Exception as e:
        print(e)
        return
    return lsts




main()


    
