#Solution by Bandara M.A.G.S.S

#Obtuse Triangles


def main():

    coordinates = get_coordinates()

    obtuse_tris = count_obtuse_triangles(coordinates)

    print(obtuse_tris)


def count_obtuse_triangles(coordinates):
    '''return number of obtuse triangles to given coordinates'''
    counter = 0

    triangles = combinations(coordinates)
    
    for triangle in triangles:
        a,b,c = triangle

        #find triangle side length's squred
        side_length_sqrd = [
            distance_sqrd(a,b),
            distance_sqrd(b,c),
            distance_sqrd(a,c)
            ]

        #check any side of triangle equal to 0
        if any(l==0 for l in side_length_sqrd):
            continue
        
        s = side_length_sqrd

        #find the obtuse condition if True increase counter by 1
        if (s[0]>s[1]+s[2] or
            s[1]>s[0]+s[2] or
            s[2]>s[0]+s[1]
            ):counter+=1

    return counter

def distance_sqrd(point1,point2):
    '''find squared of distance to given two points'''
    x1,y1 = point1
    x2,y2 = point2

    dist_sqrd = (x1-x2)**2 + (y1-y2)**2
    
    return dist_sqrd 


    
def combinations(alist):
    '''return all possible combinations to given list : note only -> (5C3)'''
    comb = []

    #simple combination algorithm
    i = 0
    for a in alist[i:3]:
        j=0
        for b in alist[1+i+j:4]:
            k=0
            for c in alist[2+i+j+k:]:
                comb.append([a,b,c])
                k+=1
            j+=1
        i+=1

    return comb
        
             
def get_coordinates():

    coordinates = []
    while True:
        inp = input().strip()

        if inp=="-1":break

        if inp=="":continue

        #after convert to integers ass coordinates to list
        x,y = map(int,inp.split())
        coordinates.append((x,y))

    return coordinates
            
main()   

