def main(inpfile):
    
    nums = readFile(inpFile)
    if nums is None:return -1
    
    digitalFormat = [getDigitalFormat(n) for n in nums]

    if showResult("result.txt",digitalFormat)==-1:return -1




def showResult(outFile,result):
    try:
        with open(outFile,"w") as file:
            for line in result:
                print(line)
                file.write(line+"\n")
    except Exception as e:
        print(e)
        return -1



def getDigitalFormat(n):
    n_str = str(n)

    digitals = [getDigital(int(num)).split("\n") for num in n_str]

    dFormat = "\n".join([" ".join(tup) for tup in zip(*digitals)])
        
    return dFormat



def getDigital(digit):

    vt = "+-+"
    
    match digit:
        case 0:
            dFormat = f"{vt}\n| |\n   \n| |\n{vt}\n"
        case 1:
            dFormat = f"   \n  |\n   \n  |\n   \n"
        case 2:
            dFormat = f"{vt}\n  |\n{vt}\n|  \n{vt}\n"
        case 3:
            dFormat = f"{vt}\n  |\n{vt}\n  |\n{vt}\n"
        case 4:
            dFormat = f"   \n| |\n{vt}\n  |\n   \n"
        case 5:
            dFormat = f"{vt}\n|  \n{vt}\n  |\n{vt}\n"
        case 6:
            dFormat = f"{vt}\n|  \n{vt}\n| |\n{vt}\n"
        case 7:
            dFormat = f"{vt}\n  |\n   \n  |\n   \n"
        case 8:
            dFormat = f"{vt}\n| |\n{vt}\n| |\n{vt}\n"
        case 9:
            dFormat = f"{vt}\n| |\n{vt}\n  |\n{vt}\n"
        case _:
            return


    return dFormat



def readFile(inpFile):
    try:
        with open(inpFile) as file:
            nums = list(map(int,(line.rstrip() for line in file) ))
    except Exception as e:
        print(e)
        return

    return nums



if __name__=="__main__":
    main(input().strip())
    #print(getDigitalFormat(1234567890))







    
