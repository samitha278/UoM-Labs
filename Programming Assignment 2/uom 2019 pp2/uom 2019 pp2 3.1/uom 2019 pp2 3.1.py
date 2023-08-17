def main():

    '''
    inpt file content:
    case 1:
    1
    Car

    case 2:
    2
    Hello world
    Hi python
    '''
    file = input().strip()     

    messages = read_file(file)
    if messages == -1: return -1

    encrypt_messages = [get_encrypt_message(message.upper()) for message in messages]

    for em in encrypt_messages:
        print(em)

    writer = write_file(encrypt_messages)
    if writer == -1 : return -1
    


def write_file(encrypt_messages):

    try:
        with open("F:\\uom 2019 pp2\\uom 2019 pp2 3\\output 3.1.txt","w") as file:
            for em in encrypt_messages:
                file.write(em+'\n')
    except:
        print("Error occurs while writing to file")
        return -1

    return 0
    

def get_encrypt_message(message):
    
    alpha = [ chr(int(ord('A'))+i) for i in range(26)] + [" "]

    em_list = []
    for c in message:
        binary = bin(alpha.index(c))[2:]
        #print(binary)
        l = len(binary)
        n = 5-l
        em_character = ['A' if char=='0' else 'B' for char in binary]
        
        em_list.append("".join(['A']*n+em_character))

    encrypt_message = "".join(em_list)
    
    return encrypt_message
           

def read_file(file):

    try:
        with open(file,"r") as file:
            messages = [each.rstrip() else each for each in file]
            n = messages.pop(0)
            #n = int(file.readline())
            #messages = [file.readline() for i in range(n)]
            
    except:
        print("Error occurs while opening file")
        return -1

    return messages


main()


    
