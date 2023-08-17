def main():

    alist = readFile(input().strip())
    if alist is None:return -1

    possi = sortList(alist)
    print(possi)

    if possi[0]:
        print("yes",possi[1][0],possi[1][1])
    else:
        print("no")



def sortList(A):

    decreSegments = findDecreasingSegments(A)
    print(decreSegments)

    for seg in decreSegments:
        l,r = seg
        Alr = A[l:r+1]
        revSegments(A,Alr,l,r)

    n = len(A)
    print(A)
    
    if all(A[i-1]<A[i] for i in range(1,n)):
        return [True,decreSegments[0]]

    return [False]


def revSegments(A,segment,l,r):

    n = len(segment)
    
    for i in range(n//2):
        A[l+i],A[r-i]=A[r-i],A[l+i]

    
   

def findDecreasingSegments(A):

    #find decreasing segment
    decreSegments = []
    
    n = len(A)
    
    p1 = p2 = 0
    decre= False

    for i in range(1,n):
        pre,now = A[i-1],A[i]

        
        if pre>now:
            p2 += 1
            decre = True
                
        else:
            if decre:
                decreSegments.append((p1,p2))
                p1=p2=i
                decre = False
            else:
                p1 += 1
                p2 += 1

    return decreSegments



    
#print(sortList([3,4,5,9,8,7,6,10,11,12,15,14,13,16,17]))
        



def readFile(inpFile):

    try:
        with open(inpFile) as file:
            alist = list(map(int,file.readline().rstrip().split(",")))
    except Exception as e:
        print(e)
        return -1
    return alist







main()
