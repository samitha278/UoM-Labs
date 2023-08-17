def main(inpFile):

    data = readFile(inpFile)
    if data is None:return -1


    output = [getOutput(line) for line in data]

    if writer("output.txt",output)==-1:return -1



def writer(outFile,output):
    try:
        with open(outFile,"w") as file:
            for line in output:
                print(line)
                file.write(line+"\n")
    except:
        return -1
    



def getOutput(line):

    ascii_val = [ord(char) for char in line]

    binary_val = [binary_8bit(n) for n in ascii_val]

    return " ".join(binary_val)


def binary_8bit(n):

    binary_rev = []

    temp = n
    
    while temp!=1:
        binary_rev.append(str(temp%2))
        temp//=2
    else:
        binary_rev.append(str(temp))

    balance = 8-len(binary_rev)
    bin_8bit = ["0"]*balance + binary_rev[::-1]
    
    bin_8bit_str = "".join(bin_8bit)

    return bin_8bit_str



    




def readFile(inpFile):

    try:
        with open(inpFile) as file:
            data = [line.rstrip() for line in file]

    except Exception as e:
        print(e)
        return
    return data



main(input().strip())
