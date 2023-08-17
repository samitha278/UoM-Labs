def main(inpFile):
    
    data = readFile(inpFile)
    if data == -1 : return -1

    n = data["n"]
    variables = data["variables"]

    rows = getRows(n)

    XOR_values = tuple(map(getXOR,rows))

    table = createTable(n,variables,rows,XOR_values)

    print(table)

    if writeFile("output.txt",table)==-1:return -1


def writeFile(outFile,output):
    try:
        with open(outFile,'w') as file:
            file.write(output)

    except Exception as e:
        print(e)
        return -1



def createTable(n,variables,rows,truth_values):

    line1 = '+'+"-+"*(n+1)+'\n'
    line2 = '|'+ '|'.join(variables) + '|Y|'+'\n'

    rest_lines = [
        '|'+ '|'.join(list(row)) + f'|{tru_val}|'+'\n'
        for row,tru_val in zip(rows,truth_values)
    ]
    table = line1+line2+line1+"".join(rest_lines)+line1.rstrip()

    return table
        



def getXOR(row):
    n = len(row)
    
    #base case
    if n==2:
        if row[0]==row[1]:
            return '0'
        else:
            return '1'

    #recursive case 
    return getXOR(getXOR(row[:2]) + row[2:])


#print(getXOR("001"))


def getRows(n):
    rows = []
    
    for i in range(2**n):
        i_bin = str(binary(i))
        l = len(i_bin)
        diff = n-l

        rows.append("0"*diff+i_bin)
        
    return tuple(rows)


def binary(number):
    if number < 0:return -1
    if number ==0:return "0"
    if number == 1:return "1"
    
    temp = number
    bin_ = []

    while temp!=1:
        bin_.append(f"{temp%2}")
        temp//=2
    else:
        bin_.append("1")
    
    return "".join(bin_[::-1])
    

#print(binary(9))
#print(getRows(5))    
    

def readFile(inpFile):

    try:
        with open(inpFile) as file:
            n = int(file.readline().rstrip())

            if n<2:raise Exception("n not be less than 2!")

            variables = file.readline().rstrip().split()
    except Exception as e:
        print(e)
        return -1
    
    return {"n":n,"variables":variables}
        

    

if __name__=="__main__":
    main(input().strip())
