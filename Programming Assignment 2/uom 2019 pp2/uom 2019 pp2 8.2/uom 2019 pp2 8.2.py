def main(inpFile):

    textData = readFile(inpFile)
    if textData is None:return -1
    
    do_ops = [doRotate(data) for data in textData]

    result = [getResult(lst) for lst in do_ops]
    
    if showResult("result.txt",result) == -1 :return -1



def showResult(outFile,output):
    try:
        with open(outFile,'w') as file:
            for line in output:
                print(line)
                file.write(line+'\n')
    except Exception as e:
        print(e)
        return -1



def getResult(lst):

    n = len(lst)

    line = '+'+'-+'*n
    sdLine = '|'+"|".join(map(str,lst))+'|'

    return "\n".join([line,sdLine,line])
   
    
    

def doRotate(data):

    operation = data["operation"]
    op_time = data["rotater"]
    numbers = data["numbers"]

    n = len(numbers)
    
    if operation == "R":
        for _ in range(op_time):
            temp = numbers[-1]

            count = n-1
            while count>0:
                numbers[count] = numbers[count-1]
                count-=1

            numbers[0] = temp
            
    elif operation=="L":
        for _ in range(op_time):
            temp = numbers[0]

            count = 0
            while count<n-1:
                numbers[count] = numbers[count+1]
                count+=1

            numbers[-1] = temp


    return numbers
        

           

    


def readFile(inpFile):

    try:
        with open(inpFile) as file:
            n = int(file.readline().rstrip())

            lines = []
            for _ in range(n):
                temp = file.readline().rstrip().split()

                op = temp[0]
                op_time = int(temp[1])
                num_list = list(map(int,temp[2:]))

                data_dic = {
                    "operation":op,
                    "rotater":op_time,
                    "numbers":num_list
                    }
                lines.append(data_dic)
                            
    except Exception as e:
        print(e)
        return

    return lines





if __name__=="__main__":
    main(input().strip())

    #data = {"operation":"L","rotater":3,"numbers":[1,2,3,4,5]}
    #print(doRotate(data))













    
