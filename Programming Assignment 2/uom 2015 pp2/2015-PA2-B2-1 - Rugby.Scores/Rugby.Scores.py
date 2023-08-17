def main():

    score = readFile(input().strip())
    if score is None:return -1

    
    combi= getCombi(score)

    if combi==-1:
        result = ["INVALID SCAORE"]
    else:
        result = [f"{key}: {val}" for key,val in combi.items() if val!=0]
    
    if writer("result.txt",result)==-1:return -1




def writer(outFile,output):
    try:
        with open(outFile,"w") as file:
            for line in output:
                print(line)
                file.write(line+"\n")
    except:
        return -1



def getCombi(score):

    combi = {"Try":0,"Conversions":0,"Penalty/Drop Goals":0}

    temp = score
    
    while temp>0:
        
        if temp>=7:
            temp-=7
            combi["Try"]+=1
            combi["Conversions"]+=1
        elif temp>=5:
            temp-=5
            combi["Try"]+=1
        elif temp>=3:
            temp-=3
            combi["Penalty/Drop Goals"]+=1
        else:
            return -1

    return combi
        
            
            
        
        
        
        




def readFile(inpFile):
    try:
        with open(inpFile) as file:
            score = int(file.readline().rstrip())

    except Exception as e:
        print(e)
        return

    return score









main()
