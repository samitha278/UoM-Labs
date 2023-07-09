#Solution by Bandara M.A.G.S.S

#H.Potter and Ginny

def main():
    encoded_message = get_encoded_msg()

    letter_set = set(encoded_message)-{" "}

    sorted_list = sort_letters(list(letter_set))

    decode_message = replace_letters(encoded_message,sorted_list)

    print(decode_message)

def replace_letters(encoded_str,sorted_list):
    swap_list = sorted_list[::-1]

    decode_list  = [swap_list[sorted_list.index(c)] if c!=" " else " " for c in encoded_str]

    decode_message = "".join(decode_list)

    return decode_message
    

def sort_letters2(alist):

    ascii_dic = {ord(char):char for char in alist}

    ascii_list = list(ascii_dic.keys())
    n = len(ascii_list)
    
    sorted_ascii_list = []
    
    for i in range(n):
        value = min(ascii_list)
        sorted_ascii_list.append(value)
        ascii_list.remove(value)

    sorted_letters = [ascii_dic[value] for value in sorted_ascii_list]

    return sorted_letters

###################################################################

def sort_letters(alist):

    sorted_list = [chr(i) for i in range(ord('A'),ord('Z')+1) if chr(i) in alist]

    return sorted_list

###################################################################

def get_encoded_msg():
    msg = input().strip()

    if all(c.isupper() or c==" " for c in msg):
        return msg
    else:
        print("Invalid message")

if __name__=="__main__":
    main()
