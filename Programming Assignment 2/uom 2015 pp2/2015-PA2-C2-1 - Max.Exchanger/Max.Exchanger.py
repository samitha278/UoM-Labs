def main():

    lst = readFile(input().strip())
    if lst is None:return -1

    exchanger(lst)

    if writer("result.txt",lst)==-1:return -1

    




def writer(outFile,output):
    try:
        with open(outFile,"w") as file:
            print(output)
            file.write(output)
    except:
        return -1




def exchanger(lst):


    temp = lst.copy()
    
    for j in range(3):

        minimum = min(temp)
        maximum = max(temp)

        temp.remove(minimum)
        temp.remove(maximum)

        i,j = lst.index(minimum),lst.index(maximum)

        lst[i],lst[j] = lst[j],lst[i]

    
                    

        
                    
                    

                
    




def readFile(inpFile):
    try:
        with open(inpFile) as file:
            lst = list(map(int,file.readline().rstrip().split()))

    except Exception as e:
        print(e)
        return

    return lst









main()
