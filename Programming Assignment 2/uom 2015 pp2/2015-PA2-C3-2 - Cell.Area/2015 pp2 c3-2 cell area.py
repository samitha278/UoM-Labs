import time


def main(inpFile):
    
    
    rectangles = getText(inpFile)
    if rectangles is None:return -1

    cells = countCells(rectangles)

    if show("result.txt",cells) == -1:return -1

    



def show(outFile,output):
    print("#cells:",output)
    
    try:
        with open(outFile,'w') as file:
            file.write(str(output))
        
    except:return -1    


def countCells(rectangles):
    cells = set()

    for rectangle in rectangles:
        
        lower_x,lower_y = rectangle[0]
        upper_x,upper_y = rectangle[1]

        for y in range(lower_y,upper_y+1):
            for x in range(lower_x,upper_x+1):
                cells.add((x,y))
        
    return len(cells)
    
    



def getText(inpFile):

    try:
        with open(inpFile) as file:

            rectangles = []

            for line in file:
                n = list(map(int,line.rstrip().split()))

                if any(num>=100 for num in n):
                    raise ValueError("coordinate must less than or equal 100")

                rectangle = [tuple(n[i*2:i*2+2]) for i in range(len(n)//2)]

                rectangles.append(rectangle)
                
            
    except Exception as e:
        print("Error occured while reading file\n",e)
        return

    return rectangles
            

if __name__=="__main__":
    main(input().strip())
    #print(getText("FileIn.txt"))
    time.sleep(5)







    
