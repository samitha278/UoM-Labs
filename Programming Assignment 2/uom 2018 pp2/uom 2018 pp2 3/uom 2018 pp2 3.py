def main(inpFile):

    indicies = readFile(inpFile)
    if indicies is None:return -1
    
    
    
    n = max(indicies)
    m = [0]*(n+1)
    f = [0]*(n+1)

    female = [Female(index,f,m) for index in indicies]
    male = [Male(index,f,m) for index in indicies]



    result = [f"{n}: F={F} M={M}"
        for n,F,M in zip(indicies,female,male)
    ]

   


    if writer("result.txt",result)==-1:return -1

    



def writer(outFile,result):

    try:
        with open(outFile,"w") as file:
            for line in result:
                print(line)
                file.write(line+"\n")

    except Exception as e:
        print(e)
        return -1
    


def Female(n,f,m):
    
    if n==0:return 1
    if f[n] !=0:return f[n]
    
    
    for i in range(1,n+1):
        f[i] = i - Male(f[i-1],f,m)

    return f[n]
    
    

def Male(n,f,m):

    if n==0:return 0
    if m[n] !=0:return m[n]
    
    
    for i in range(1,n+1):
        m[i] = i - Female(m[i-1],f,m) 

    return m[n]

    
    
def readFile(inpFile):    

    try:
        with open(inpFile) as file:
            data = [int(line.rstrip()) for line in file]

    except Exception as e:
        print(e)
        return
    

main(input().strip())

import time
time.sleep(5)
