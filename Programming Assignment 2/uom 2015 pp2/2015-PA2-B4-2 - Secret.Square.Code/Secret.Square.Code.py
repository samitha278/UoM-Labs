
def main():

    lst = readFile(input().strip())
    if lst is None:return -1

    msg = decodeMsg(lst)


    if writer("result.txt",msg)==-1:return -1




def writer(outFile,output):
    try:
        with open(outFile,"w") as file:
            print(output,end= " ")
            file.write(output+" ")
    except:
        return -1



def decodeMsg(lst):

    maxlen = max((len(word) for word in lst))

    grid = [list(word)+[""]*(maxlen-len(word)) for word in lst]

    msg = "".join("".join(row) for row in zip(*grid))

    return msg
    

    


def readFile(inpFile):
    try:
        with open(inpFile) as file:
            n = int(file.readline().rstrip())
            lst = file.readline().rstrip().split()

    except Exception as e:
        print(e)
        return

    return lst









main()
