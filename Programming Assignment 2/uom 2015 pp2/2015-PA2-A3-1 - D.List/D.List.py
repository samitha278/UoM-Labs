def main():

    data = readFile(input().strip())
    if data is None:return -1

    lst = data["list"]
    n = data["n"]


    subs = getSubLists(lst,n)

    domins = [getDominant(sub) for sub in subs]   

    result = getResult(domins,len(lst))
    

    if writer("result.txt",result)==-1:return -1




def writer(outFile,output):
    try:
        with open(outFile,"w") as file:
            print(output)
            file.write(output)

    except:
        return -1




def getResult(domins,l):
    count = {}
    for i in domins:
        try:
            count[i]+=1
        except:
            count[i]=1

    keys = count.keys()
    
    return [count[i+1] if (i+1) in keys else 0 for i in range(l)]
    
    

def getDominant(sub):

    count = {}
    for i in sub:
        try:
            count[i]+=1
        except:
            count[i]=1

    maxFreq = max(count.values())

    dominant = min([key for key,val in count.items() if val==maxFreq])

    return dominant
    

    

def getSubLists(lst,n):

    l = len(lst)

    subs = [lst[i:i+n] for i in range(l-n+1)]

    return subs
    



def readFile(inpFile):
    try:
        with open(inpFile) as file:
            lst = list(map(int,file.readline().rstrip().split()))
            n = int(file.readline().rstrip())

            l = len(lst)
            if not 0<n<l:
                raise Exception

    except Exception as e:
        print(e)
        return
    return {"list":lst,"n":n}










main()
