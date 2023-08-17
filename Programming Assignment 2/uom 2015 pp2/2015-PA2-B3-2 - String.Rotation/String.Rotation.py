def main():
    
    try:
        with open(input().strip()) as file:
            strings = [line.rstrip() for line in file]
    except Exception as e:
        print(e)
        return -1

     

    grid = getGrid(strings)

    transGrid = getTranspose(grid)

    result = getResult(transGrid)

    for line in result:
        print(line)



def getResult(grid):

    lines = []
    
    for row in grid:
        line = "".join((" " if c=='0' else c for c in row ))
        lines.append(line)
    return lines
    
        




def getTranspose(grid):

    return [list(row) for row in zip(*grid)]
        







def getGrid(strings):

    maxlen = max(len(string) for string in strings)
    l = len(strings)

    grid = [list(strings[i])+['0']*(maxlen-len(strings[i])) for i in range(l)] 

    return grid







main()
