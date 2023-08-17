def main(inpFile):

    players = readFile(inpFile)
    if players is None: return -1

    ranks = list(map(getRank,players))

    r1,r2 = ranks
    output = f"{r1} {r2}"

    if show("result.txt",output)==-1:return -1
    



def show(outFile,output):
    try:
        with open(outFile,'w') as file:
            print(output)
            file.write(output+"\n")
    except:
        return -1





def getRank(cards):

    cards_dic = [{"suit":card[1],"value":card[0]} for card in cards]

    suits = [card["suit"] for card in cards_dic]
    values = [card["value"] for card in cards_dic]

    orderP1 = [str(i) for i in range(2,10)]
    orderP2 = ['T','J','Q','K','A']
    order = orderP1 + orderP2

    
    #Rank 3 & Rank 5 & Rank 6
    rank3 = False
    
    suit_1 = suits[0]
    if all(suit_1==suit for suit in suits):

        #Rank 6
        if all(val in orderP2 for val in values):
            return 6
        

        #Rank 5
        #sort values
        temp = values.copy()
        temp.sort(key = lambda x:order.index(x))
        #print(temp)

        #create sub list 
        u = order.index(temp[0])
        sub_order = order[u:u+5]

        #evaluate rank 5 condition    
        if all(x==y for x,y in zip(temp,sub_order)):
            return 5

        
        #Rank 3
        rank3 = True

        

    #Rank 2
    rank2 = False 
    for i in values:
        if values.count(i)==3:
            rank2 = True
            break
        
    #Rank 4
    if rank2:
        set_val = set(values)
        counts = [values.count(i) for i in set_val]
        
        if [i>=2 for i in counts].count(True) == 2:
            return 4

        return 2

    


    
    return 1
    
    
    

    
        





    
    



def readFile(inpFile):               
    try:
        with open(inpFile) as file:
            line = file.readline().rstrip().split()
            player1 = line[:5]
            player2 = line[5:]
            
            players = [player1,player2]
    except Exception as e:
        print(e)
        return

    return players 
    



if __name__=="__main__":
    main(input().strip())













