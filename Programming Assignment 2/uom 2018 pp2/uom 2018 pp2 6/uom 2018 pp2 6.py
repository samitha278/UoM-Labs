def main(inpFile):

    int_list = readFile(inpFile)
    if int_list is None:return -1
    

    lists = getGroups(int_list)

    if writer("output.txt",lists) == -1:return -1





def writer(outFile,output):
    try:
        with open(outFile,"w") as file:
            for line in output:
                print(line)
                file.write(str(line)+"\n")
    except Exception as e:
        print(e,"k")
        return -1



    
    


def getGroups(lst):
    l = len(lst)
    
    groups = [
        [[lst[i],lst[j],lst[k]],[i,j,k]]
        for i in range(l)
        for j in range(i+1,l)
        for k in range(j+1,l)
        if lst[j]-lst[i] == lst[k]-lst[j]
    ]

    return groups
                    









def readFile(inpFile):
    try:
        with open(inpFile) as file:
            lst = list(map(int,file.readline().rstrip().split()))
    except Exception as e:
        print(e)
        return
    print(lst)
    return lst






if __name__=="__main__":
    main(input().strip())
