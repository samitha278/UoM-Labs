def main():

    data = readFile(input().strip())
    if data is None:return -1

    runs = [getTotalRuns(each) for each in data]

    print("Name        Runs")
    for dic in runs:
        print(dic["Name"] , dic["Runs"])





def getTotalRuns(dic):

    name = dic["Name"]
    
    ones = int(dic["ones"])
    two = int(dic["two"])
    three = int(dic["three"])
    four = int(dic["four"])
    six = int(dic["six"])
    
    runs = ones+2*two+3*three+4*four+6*six

    return {"Name":name , "Runs": runs}
    

    





def readFile(inpFile):

    try:
        with open(inpFile) as file:
            data = []
            
            details = file.readline().rstrip().split()


            for line in file:

                infos = line.rstrip().split()

                data.append({name:info for name,info in zip(details,infos)})
                
    except Exception as e:
        print(e)
        return        

    return data








main()
