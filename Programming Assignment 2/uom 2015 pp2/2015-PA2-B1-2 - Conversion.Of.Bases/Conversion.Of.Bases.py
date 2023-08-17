def main():

    data = readFile(input().strip())
    if data is None:return -1

    integer = data["N"]
    base = data["B"]

    number = baseConverter(base,integer)

    expansion = getExpansion(base,number)

    output = f"{number} = {expansion}"

    if writer("output.txt",output)==-1:return -1


def writer(outFile,output):
    try:
        with open(outFile,"w") as file:
            print(output)
            file.write(output)
    except:
        return -1
    



def getExpansion(base,number):
    
    expansion = " + ".join(
        [
            f"{num}*{base}^{i}"
            for i,num in enumerate(number[::-1])
        ]
    )
    

    return expansion 




def baseConverter(base,integer):

    lst = []
    
    temp = integer

    while temp!=1:
        lst.append(temp%base)
        temp//=base
    else:
        lst.append(temp)

    number = "".join(map(str,lst[::-1]))

    return number






def readFile(inpFile):
    try:
        with open(inpFile) as file:
            N,B = list(map(int,file.readline().rstrip().split()))

            if (not 1<N<100000) or (not 1<B<10):
                raise Exception
            
            data = {"N":N,"B":B}
    except Exception as e:
        print(e)
        return
    return data





main()
