def main():

    file = input().strip()
    
    data = read_file(file)
    if data == -1 :return -1
    print(data)

    string,k_str = data
    k = int(k_str)

    sub_strings = get_sub_strings(string,k)

    for sub in sub_strings:
        print(sub)
        
    writer = write_file(sub_strings)
    if writer == -1 : return -1



def write_file(data):
    
    try:
        with open("F:\\uom 2019 pp2\\uom 2019 pp2 11\\output 11.1.txt","w") as file:
            for each in data:
                file.write(each+'\n')
    except:
        print("Error occured while writing file")
        return -1

    return 0
    
        

def get_sub_strings(string,k):
    n = len(string)
    temp_sub_strings = [string[i*k:i*k+k] for i in range(n//k)]

    print(temp_sub_strings)
    
    sub_strings = []
    
    for t in temp_sub_strings:
        u = [t[0]]
        for c in t[1:]:
            if c not in u:
                u.append(c)
        sub_strings.append("".join(u))

    return sub_strings
                

    
def read_file(file):

    try:
        with open(file,"r") as file:
            data =[each[:-1] if '\n' in each else each for each in file]
    except FileNotFoundError: 
        print("Error occured while opnening file")
        return -1
    except IndexError:
        print("ggggggg")
        return -1
    return data
        
        

main()
