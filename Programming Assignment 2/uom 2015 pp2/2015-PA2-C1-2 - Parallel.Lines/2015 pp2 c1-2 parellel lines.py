def main(inpFile):

    coordinates = readText(inpFile)
    if coordinates is None:return -1

    p = coordinates["p"]
    q = coordinates["q"]

    other_coo = coordinates["other"]

    pq_gradient = getGradient(p,q)
    #print(pq_gradient)

    
    parallelLines = getParallelLines(pq_gradient,other_coo)
    if parallelLines==0:
        output = "No parallel lines"
    else:
        output = str(parallelLines)
        
    if showResult("result.txt",output)==-1:return -1
    


def showResult(outFile,output):
    print(output)

    try:
        with open(outFile,"w") as file:
            file.write(output)
    except Exception as e:
        print(e)
        return -1













#method 1
def getParallelLines(gradient,coordinates):
    
    parallelLines = [
        m
        for index,point in enumerate(coordinates[:-1])
        for coo in coordinates[index+1:]
        if (m:=getGradient(point,coo))==gradient
    ]

    return len(parallelLines)



#method 2 
def getParallelLines2(gradient,coordinates):

    gradients = []

    pointer = 0

    while pointer<len(coordinates)-1:

        for coo in coordinates[pointer+1:]:
            gradients.append(getGradient(coordinates[pointer],coo))

        pointer+=1

    parallelLines = sum(1 for gra in gradients if gradient==gra)

    return parallelLines

    










def getGradient(m,n):

    gradient = (n[1]-m[1])/(n[0]-m[0])

    return gradient




def readText(inpFile):

    try:
        with open(inpFile) as file:
            coos = [tuple(map(int,line.rstrip().split())) for line in file]

            p = tuple(coos[0][:2])
            q = tuple(coos[0][2:])

            other = coos[1:]

    except Exception as e:
        print(e)
        return 

    coordinates = {"p":p,"q":q,"other":other}
    return coordinates
    
    
    
    


if __name__=="__main__":
    main(input().strip())
    #print(readText(input()))

    






    
