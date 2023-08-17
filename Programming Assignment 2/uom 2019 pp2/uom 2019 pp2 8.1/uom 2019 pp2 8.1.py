def main(inpFile):

    text = readFile(inpFile)
    if text is None:return -1

    sString = list(map(shortendString,(tup for tup in text)))

    if show("result.txt",sString)==-1:return -1



def show(outFile,output):
    try:
        with open(outFile,'w') as file:
            for line in output:
                print(line)
                file.write(line+'\n')
    except:
        return -1
        



def shortendString(tup):
    string,index = tup
    
    l = len(string)
    
    sList = []
    count = 0 

    while count<l:
        temp = string[count]

        while count<l-1 and temp==string[count+1]:
            count+=1

        sList.append(temp)
        count+=1

    sString = "".join(sList)
    #print(sString)

    if 0<=(n:=int(index))<len(sString):
        return sString[n-1]

    return "index out of range"


    



def readFile(inpFile):

    try:
        with open(inpFile) as file:
            n = int(file.readline().rstrip())

            text = [
                tuple(file.readline().rstrip().split())
                for _ in range(n)
            ]
    except Exception as e:
        print(e)
        return

    return text
    



if __name__=="__main__":
    main(input().strip())
    #print(shortendString(("aeebvvvhkkkk",6)))
