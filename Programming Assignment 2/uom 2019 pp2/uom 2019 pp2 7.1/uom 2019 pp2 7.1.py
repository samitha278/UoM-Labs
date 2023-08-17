import string

def main(inpFile):

    #read file & get data
    data = read_file(inpFile)
    if data==-1:return -1

    #unpacking returned data dictionary
    n = data["n"]
    message = data["message"]
    key = data["matrix"]

    
    #get vector
    P = get_vector(n,message)

    #multiply P by key
    key_P_mul = matrix_mul(key,P)
    if key_P_mul==-1:return -1

    #get decode message
    decode_message = get_decode_message(key_P_mul)

    print(decode_message)

    #write to file
    if write_file("output 7.1.txt",decode_message) == -1:return -1
    



def write_file(outFile,output):
    try:
        with open(outFile,"w") as file:
            file.write(f"{output}\n")
    except Exception as e:
        print(f"Erro! {e}")
        return -1



def get_decode_message(matrix):
    KP = [row[0]%27 for row in matrix]

    decode_message = "".join([" " if n==26 else chr(n+ord("A")) for n in KP])

    return decode_message

            

def matrix_mul(mat1,mat2):
    
    a,b,c,d = len(mat1),len(mat1[0]),len(mat2),len(mat2[0])

    if b != c:return -1
    
    mul_matrix = [
        [
            sum(mat1[i][k]*mat2[k][j] for k in range(b))
            for j in range(d)
        ]
        for i in range(a)
    ]

    return mul_matrix


    
def transpose(matrix):
    
    m,n = len(matrix),len(matrix[0])

    trans = [
        [matrix[i][j] for i in range(m)]
        for j in range(n)
    ]

    return trans
    


def get_vector(n,message):
    punc = string.punctuation
    
    P_temp = [[26 if char in punc or char==" " else ord(char)-ord("A") for char in message]]

    if len(message)% n != 0:
        P_temp[0].append(26)

    P = transpose(P_temp)
        
    return P



def read_file(inpFile):
    
    try:
        with open(inpFile) as file:

            data = dict()
            
            temp = [line.rstrip() for line in file]

            data["n"] = int(temp[0])

            data["message"] = temp[1].upper()
            
            data["matrix"] = [
                list(map(int,row.split()))
                for row in temp[2:]
            ]

    except Exception as e:
        print(f"Error! {e}")
        return -1

    print(data)

    return data
        


if __name__=="__main__":
    main(input().strip())
