
def main():

    lst = readFile(input().strip())
    if lst is None:return -1

    

    
    inOrderWords = [word for word in lst if isInOrderWord(word)]




    if writer("result.txt",inOrderWords)==-1:return -1




def writer(outFile,output):
    try:
        with open(outFile,"w") as file:
            for line in output: 
                print(line,end= " ")
                file.write(line+" ")
    except:
        return -1



def isInOrderWord(word):

    word_lst = [c for c in word if c.isalpha()] 
    word = "".join(word_lst)
    
    word_lst.sort()

    sword = "".join(word_lst)

    return word==sword
    
    



    


def readFile(inpFile):
    try:
        with open(inpFile) as file:
            lst = file.read().rstrip().split()

    except Exception as e:
        print(e)
        return

    return lst









main()
