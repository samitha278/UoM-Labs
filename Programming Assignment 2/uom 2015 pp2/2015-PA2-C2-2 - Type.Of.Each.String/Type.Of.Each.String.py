def main():

    try:
        with open(input().strip()) as file:
            lines = [line.rstrip() for line in file]

    except:
        return -1


    types = [getType(line) for line in lines]

    for l in types:
        print(l)







def getType(line):
    if '-' in line:
        #print(line,"datechecker")
        if isDate(line):
            return "date"
        return "text"
        

    if '.' in line:
        #print(line,"floatchecker")
        if isFloat(line):
            return "float"
        return "text"

    

    if isFloat(line+".0"):
        #print(line,"intchecker")
        return "int"

    return "text"



def isDate(line):
    l = len(line)
    if l != 10:
        return False

    count = sum((1 for c in line if c=='-'))
    if count!=2:
        return False

    dd,mm,yyyy = list(map(int,line.split("-")))

    if not (0<dd<32 and 0<mm<13 and 1991<yyyy<2999):
        return False


    return True


def isFloat(line):
    
    if '-' in line or '+' in line:
        line = line[1:]

    #print(line)
    
    parts = line.split(".")
    if len(parts)!=2:
        return False

    digits = [str(i) for i in range(10)]

    for part in parts:
        for c in part:
            if c not in digits:
                return False

    return True

    
    
        
    















main()

        










