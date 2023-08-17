def main(inpFile):

    data = readFile(inpFile)
    if data is None:return -1
    #print(data)


    rearranged_lists = [rearrange(dic) for dic in data]
    #print(rearranged_lists)

    if writer("output.txt",rearranged_lists)==-1 : return -1




def writer(outFile,output):
    try:
        with open(outFile,"w") as file:
            for line in output:
                print(line)
                file.write(str(line)+"\n")

    except Exception as e:
        print(e)
        return -1

    



def rearrange(dic):

    lst = dic["list"]
    x = dic["x"]
    y = dic["y"]

    n = len(lst)

    y_ind = [i for i in range(n) if lst[i]==y]
    
    for i in range(n-1):

        if lst[i]==x:
            lst[y_ind.pop(0)] = lst[i+1]
            lst[i+1] = y

    return lst



def readFile(inpFile):
    try:
        with open(inpFile) as file:

            lines = [line.rstrip() for line in file]

            data = []
            
            for line in lines:
                temp = line.split()
                lst = temp[0][1:-1].split(",")
                data.append({
                    "list":list(map(int,lst)),
                    "x":int(temp[1]),
                    "y":int(temp[2])
                })
                

    except Exception as e:
        print(e)
        return

    return data
        






if __name__=="__main__":
    main(input().strip())
