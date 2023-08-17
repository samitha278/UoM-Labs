def main(inpFile):

    time = readFile(inpFile)
    if time==-1:return -1
    
    dig_for = [digitalFormat(getDigitalTime(one)) for one in time]

    for t in dig_for:
        print(t)
        
    if writeFile("output.txt",dig_for)==-1:return -1
    



def writeFile(outFile,output):
    try:
        with open(outFile,'w') as file:
            for line in output:
                file.write(line)
    except:
        return -1



def digitalFormat(digitalTime):

    nums = "".join(digitalTime.split(':'))

    dts = list(map(getFormat,nums))
    
    a,b,c,d = dts
    firstLine = a[:2] + " "*2 + b[:2] + " "*4 + c[:2] + " "*2 + d[:2] + '\n'
    secondLine = a[3:6] + " " + b[3:6] + " . " + c[3:6] + " " + d[3:6] + '\n'
    thirdLine = a[7:10] + " " + b[7:10] + " . " + c[7:10] + " " + d[7:10] + '\n'
 
    return firstLine+secondLine+thirdLine
    
        
    


def getFormat(digit):
    if digit=='.':return '.'
    
    pos = list(" _\n|_|\n|_|")
    
    match digit:
        case '0':
            pos[4] = ' '
            
        case '1':
            for i in range(10):
                if i in [0,2,6,5,9]:continue
                pos[i]=' '
                
        case '2':
            pos[3],pos[9]=' ',' '
            
        case '3':
            pos[3],pos[7]=' ',' '
            
        case '4':
            pos[1],pos[7],pos[8]=' ',' ',' '

        case '5':
            pos[5],pos[7]=' ',' '
            
        case '6':
            pos[5]=' '
            
        case '7':
            for i in range(10):
                if i in [0,2,6,1,5,9]:continue
                pos[i]=' '
            
        case '8':
            pass
        case '9':
            pos[7],pos[8]=' ',' '
            
        case '_':return -1

    return "".join(pos)
     
#print(getFormat('7'))

def getDigitalTime(time):

    am = time.endswith("am")
    digital = time.removesuffix("am") if am else time.removesuffix("pm")
    parts = list(digital.partition('.'))
    
    if am:
        if (hour:=parts[0])=='12':parts[0]='00'
        if len(hour)==1:parts[0]='0'+hour
        
    else:
        hour = int(parts[0])
        if hour!=12:parts[0] = str(hour+12)
        
        
    parts[1]=':'    
    digital = ''.join(parts)
    return digital


#print(getDigitalTime("12.44pm"))


def readFile(inpFile):

    try:
        with open(inpFile) as file:
            time = [line.rstrip() for line in file]
    except Exception as e:
        print("Error",e)
        return -1
    else:
        return time

#print(readFile("input.txt"))


if __name__=="__main__":
    main(input().strip())
