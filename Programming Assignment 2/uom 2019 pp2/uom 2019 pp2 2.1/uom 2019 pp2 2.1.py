def main(inpFile):

    positions = readFile(inpFile)
    if positions is None: return -1

    otherPos = getPositions(positions)

    if show("result.txt",otherPos)==-1:return -1




def show(outFile,output):
    try:
        with open(outFile,'w') as file:
            for tup in output:
                x,y=tup
                line = f"{x}{y}"
                print(line)
                file.write(line+'\n')
    except:
        return -1
    


    

    


def getPositions(positions):

    allPositions_temp = list(map(getpaths,positions))

    allPositions = []
    for pos in allPositions_temp:
        allPositions.extend(pos)

    allPositions = set(allPositions)
    
    #print(f"all positions ======='\n' {allPositions}")

    ran = range(8)
    chessBoard = set([
        (i,j)
        for i in ran
        for j in ran
    ])

    diff = list(chessBoard - allPositions)

    remains = []
    alpha = [chr(i) for i in range(ord('a'),ord('a')+8)]

    for tup in diff:
        x,y = tup
        new_tup = (alpha[x],y+1)
        remains.append(new_tup)

    remains.sort(key = lambda x:x[0])

    return remains
    



def getpaths(position):
    x,y = position[0],int(position[1])-1
    
    alpha = [chr(i) for i in range(ord('a'),ord('a')+8)]
    x = alpha.index(x)

    
    vert = [(x,n) for n in range(8)] 
    hori = [(n,y) for n in range(8)]

    di1 = []
    i,j = x,y
    while i<8 and j<8:
        di1.append((i,j))
        i+=1
        j+=1
        
    i,j = x,y
    while -1<i and -1<j:
        di1.append((i,j))
        i-=1
        j-=1

    
    di2 = []
    i,j = x,y
    while -1<i and j<8:
        di2.append((i,j))
        i-=1
        j+=1
        
    i,j = x,y
    while i<8 and -1<j:
        di2.append((i,j))
        i+=1
        j-=1

    allpos = list(set(vert+hori+di1+di2))


    #print(f"{position}--------{allpos}")

    return allpos


    
    
    
    















def readFile(inpFile):
    try:
        with open(inpFile) as file:
            positions = file.readline().rstrip().split()

    except Exception as e:
        print(e)
        return

    return positions





    





if __name__=="__main__":
    main(input().strip())
