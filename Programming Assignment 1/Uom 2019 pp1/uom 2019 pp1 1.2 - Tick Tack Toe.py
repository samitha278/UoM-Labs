#Solution by Bandara M.A.G.S.S

#Tick Tack Toe




def play_game():
    '''tick tack toe game function'''

    #main dictionary to route game
    dic = {
        1:"_ ",2:"_ ",3:"_ ",
        4:"_ ",5:"_ ",6:"_ ",
        7:"_ ",8:"_ ",9:"_ "
        }

    #print dictionary
    print_dict(dic)
    
    counter = 0

    #loop break when certain conditions met
    while True:
        #input number from player 1 and player 2
        num = int(input())
        
        if counter%2==0:
            dic[num] = "X "
        else:
            dic[num] = "O "

        #print dictionary
        print_dict(dic)

        #increasing counter by 1
        counter += 1

        #check who wins or not (you can use method 1 or 2)
        if checker(dic):
            break
        
        if counter == 9:
            print("Draw!")
            break

    return 0




def print_dict(dic):
    '''print given dictionary's value like 3*3 squre'''

    for num in dic:
        print(dic[num],end="")

        if num%3==0:
            print()
    return 0


    

#method 1
def checker(dic):
    '''check who wins according to given dictionary'''
    alist = ["X ","O "]

    b_value = False

    #check all wining conditions
    for index,j in enumerate(alist):

        #check horizontal conditions
        for i in range(3):
            condition_1 = dic[1+3*i]==j and dic[2+3*i]==j and dic[3+3*i]==j
            condition_2 = dic[1+i]==j and dic[4+i]==j and dic[7+i]==j

            if condition_1 or condition_2:
                print(f"player {index+1} wins!!")
                b_value = True
                
        #check diagonal conditions    
        for i in range(2):
            condition_3 = dic[1+i*2]==j and dic[5]==j and dic[9-i*2]==j

            if condition_3:
                print(f"player {index+1} wins!!")
                b_value = True

    return b_value





#method 2
alst = ['X','O']

winning_positions = [
                    [1,2,3],[4,5,6],[7,8,9],   #horizontal
                    [1,4,7],[2,5,8],[3,6,9],    #vertical
                    [1,5,9],[3,5,7]             #diagonal
                    ]
def checker2(dic):
    global alst,winning_positions
    for index,c in enumerate(alst):
        for wp in winning_positions:
            if all(dic[i].strip()==c for i in wp):
                print(f"player {index+1} wins!!")
                return True
    return False


        

#driver code
if __name__ == '__main__':
    play_game()
