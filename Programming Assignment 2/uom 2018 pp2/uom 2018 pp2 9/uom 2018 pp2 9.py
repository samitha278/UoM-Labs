def main():

    data = readFile(input().strip())
    if data is None:return -1


    ks = [getK(dic["integer"],dic["fractionList"]) for dic in data]
    
    for k in ks:
        print(k)




def getK(k,fractions):

    denominators = [frac[1] for frac in fractions]
    numerators = [frac[0] for frac in fractions]

    count = 1 
    while count<51:

        for frac in fractions:
            numer,deno = frac
            if k%deno==0:
                k = (k//deno)*numer
                break
        else:
            return k
        
        count+=1

    return k




def readFile(inpFile):

    try:
        with open(inpFile) as file:
            data = []
            
            for line in file:
                temp = line.split("|")    
                integer = int(temp[0])
                fractionList = [tuple(map(int,frac.split("/"))) for frac in temp[1].split(",")]

                data.append({
                    "integer":integer,
                    "fractionList":fractionList            
                })

    except Exception as e:
        print(e)
        return
    return data
                



main()
