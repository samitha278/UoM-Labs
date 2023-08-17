def main():

    positions = readFile(input().strip())
    if positions is None:return -1

    rev_pos = [reverseOrder(position) for position in positions]

    ranks = [getRanks(lst) for lst in rev_pos]
    
    with open("output.txt","w") as file:
        for line in ranks:
            print(line)
            file.write(str(line)+"\n")


def getRanks(lst):

    l = len(lst)
    ranks = [i for i in range(1,l+1)]

    temp = ranks.copy()
    
    for i in range(l-1,-1,-1):
        new_pos = i+lst[i]
        temp.insert(new_pos,temp.pop(i))
        

    return temp
            
        
#print(getRanks([1,1,0,0]))
    

    
    




def reverseOrder(position):

    revLst = position.copy()

    for i in range(len(position)):

        temp = revLst.pop(i)
        new_pos = i-temp
        revLst.insert(new_pos,temp)

    return revLst
        

     
    
#print(reverseOrder([0,1,2,0,1]))    









def readFile(inpFile):
    try:
        with open(inpFile) as file:
            pos = [list(map(int,line.strip().split())) for line in file]
    except Exception as e:
        print(e)
        return

    return pos



main()
