#Solution by Bandara M.A.G.S.S

#Circles,Squares

def main():

    grid = get_line()

    circle = get_line()

    if len(circle)==3 and len(grid)==2:
        
        width,height = grid[0],grid[1]
        center,radius = tuple(circle[:2]),circle[-1]
        
    else:
        return f"Invalid Input"

    squares = count_squares(width,height,center,radius)

    print(squares)


def count_squares(width,height,center,radius):
    '''calculate how many squares in given circle and grid'''
    center_x,center_y = center[0],center[1]

    #calculate grid coordinates which contain circle
    x1,x2 = center_x-radius,center_x+radius
    y1,y2 = center_y-radius,center_y+radius

    squares = set()
    squared_radius = radius**2
    
    for x in range(x1,x2):
        if 0<=x<width:
            for y in range(y1,y2):
                if 0<=y<height:

                    squared_distance = (center_x - (x + 0.5))**2 + (center_y - (y + 0.5))**2
                    if squared_distance <= squared_radius:
                        squares.add((x, y))

    return len(squares)


def get_line():
    '''get user input and return integer list'''
    line = list(map(int,input().strip().split()))
    return line
    
main()
