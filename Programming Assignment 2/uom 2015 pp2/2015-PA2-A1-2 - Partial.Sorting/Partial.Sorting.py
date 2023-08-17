def main():

    data = readFile(input().strip())
    if data is None:return -1

    x = data["x"]
    alist = data["list"]

    partiallySort(x,alist)

    print(alist)

    

def partiallySort(x,alist):
    
    n = len(alist)
    pivot = alist[x]

    i = 0
    left = x
    while i<x:
        print(alist)
        temp = alist[i]
        
        if temp>pivot:
            j = i
            
            while j<left:
                alist[j] = alist[j+1]                
                j+=1

            alist[j] = temp
            i-=1
            x-=1
        i+=1

    i = left+1

    while i<n:
        print(alist)
        temp = alist[i]

        if temp<pivot:
            j = i
            
            while x<j:
                alist[j] = alist[j-1]                
                j-=1
            
            x+=1
            alist[j] = temp
            
        i+=1
         
    
    

    

def readFile(inpFile):
    try:
        with open(inpFile) as file:
            x_str,alist_str = [line.rstrip() for line in file] 

            x = int(x_str)
            alist = list(map(int,alist_str.split()))

            n = len(alist)
            if not 0<n<100:
                raise Exception
            

            if not 0<=x<n:
                raise Exception

    except Exception as e:
        print(e)
        return

    return {"x":x,"list":alist} 
            

main()
