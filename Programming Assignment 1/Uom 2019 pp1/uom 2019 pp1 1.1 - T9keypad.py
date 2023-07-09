#Solution by Bandara M.A.G.S.S

#T9keypad


def main():
    string = input("")

    time = cal_time(string.lower())

    print("%.2f" % time)

    

def cal_time(string):
    '''return time taken to type given message'''
    
    #databse as dictionary key=character, value=(key number,positon) 
    dic = {
        "a" :(2,1),"b" :(2,2),"c":(2,3),
        "d" :(3,1),"e" :(3,2),"f":(3,3),
        "g" :(4,1),"h" :(4,2),"i":(4,3),
        "j" :(5,1),"k" :(5,2),"l":(5,3),
        "m" :(6,1),"n" :(6,2),"o":(6,3),
        "p" :(7,1),"q" :(7,2),"r":(7,3),"s":(7,4),
        "t" :(8,1),"u" :(8,2),"v":(8,3),
        "w" :(9,1),"x" :(9,2),"y":(9,3),"z":(9,4),
        "." :(1,1),
        " " :(0,1),
        }
    
    time = 0.2 * (dic[string[0]][1])  #fist charcater's time 
    
    previous_key = dic[string[0]][0]  #first character's key

    for char in string[1:]:  

        current_key = dic[char][0]    #current charaacter's key
        char_posi = dic[char][1]      #current character's position in key
        
        if current_key != previous_key:
            time +=  0.4 + 0.2 * char_posi  #move time + press time * position in key
        else:
            time += 0.7 + 0.2 * char_posi  #wait time + press time * position in key

        previous_key = current_key    #update previous key

    return time


#driver code
if __name__ == '__main__':
    main()
