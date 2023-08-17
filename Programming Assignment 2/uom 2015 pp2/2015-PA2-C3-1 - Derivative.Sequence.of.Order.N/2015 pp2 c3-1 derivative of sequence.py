def main(inpFile):
    
    
    text = getText(inpFile)
    if text is None:return -1

    sequence = text["sequence"]
    N = text["N"]

    derivative = getDerivative(sequence,N)
    #print(derivative)

    for i in derivative:
        print(i,end = " ")

    if show("result.txt",derivative)==-1:return -1



def show(outFile,output):
    try:
        with open(outFile,'w') as file:
            for i in output:
                file.write(str(i)+" ")
        
    except:return -1    
   

def getDerivative(sequence,N):

    temp = sequence
 
    for _ in range(N):
        k = len(temp)
        derivative = [temp[i+1]-temp[i] for i in range(k-1)] 
        temp = derivative

    return derivative




def getText(inpFile):

    try:
        with open(inpFile) as file:
            sequence = list(map(int,file.readline().rstrip().split()))

            if not 1<=(k:=len(sequence))<=100:
                raise ValueError(
                    "length of sequence must be greater than 1 and less than 100"
                    )
            
            N = int(file.readline().rstrip())

            if not N<k:
                raise ValueError("N must be less than length of sequence")
            
    except Exception as e:
        print("Error occured while reading file\n",e)
        return

    return {"sequence":sequence,"N":N}
            

if __name__=="__main__":
    main(input().strip())
    #print(getText("FileIn.txt"))
    







    
