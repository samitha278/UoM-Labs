
def main():

    X = readFile(input().strip())
    if X is None:return -1

    
    answer = getSmallestDecimal(X)



    if writer("result.txt",answer)==-1:return -1




def writer(outFile,output):
    try:
        with open(outFile,"w") as file:
             print(output,end= " ")
             file.write(output+" ")
    except:
        return -1



def getSmallestDecimal(X):

    Xbinary32 = format(X,"032b")

    Xcount = Xbinary32.count("1")

    N = X+1
    while True:
        Nbinary32 = format(N,"032b")
        Ncount = Nbinary32.count("1")

        if Ncount==Xcount:
            return N

        N+=1

    


def readFile(inpFile):
    try:
        with open(inpFile) as file:
            num = int(file.read().rstrip())

    except Exception as e:
        print(e)
        return

    return num









main()
