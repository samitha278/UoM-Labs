def main(inpFile):
    strings = getText(inpFile)
    if strings is None:return -1

    result = list(map(longestSubString,strings))

    if showResult("result.txt",result)==-1:return -1
    

    
def showResult(outFile,output):
    try:
        with open(outFile,'w') as file:
            for line in output:
                print(line)
                file.write(line+'\n')
    except:
        return -1
    


def longestSubString(string):

    n = len(string)

    longestSub = ""
    
    pointer = 0
    
    while pointer<n-2:

        temp = list(temp_str:=string[pointer:pointer+2])

        count = pointer
        lowertemp = temp_str.lower()
        if lowertemp[0]==lowertemp[1]:
            temp.append(string[pointer+2])
            count+=1

        for i in range(count+2,n):
            x = string[i]
            
            if (x.lower() in temp) or (x.upper() in temp):
                temp.append(x)
            else:
                break

        subString = "".join(temp)

        if len(subString)>=len(longestSub):
            longestSub = subString

        pointer+=1

    return longestSub 
            
#print(longestSubString("aBbcCc"))


def getText(inpFile):
    try:
        with open(inpFile) as file:
            strings = [line.rstrip() for line in file] 

        if any(not line.isalpha() for line in strings):
            raise ValueError("string does not contain non-alphabetic characters")

    except Exception as e:
        print(e)
        return None

    return strings




#driver code
if __name__=="__main__":
    main(input().strip())
    #pass
