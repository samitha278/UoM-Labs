#Solution by Bandara M.A.G.S.S

#3Vector

def main():
    points = get_points(4)

    vectors = get_vectors(points)

    p,q,r = vectors

    #ckeck p,q,r vectors are colinear using cross product
    if all(i==0 and j==0 for i,j in zip(get_cross_prod(p,q),get_cross_prod(q,r))):
        print("All the points are colinear")
        return 0

    scalar_tp = get_scalar_triple_product(vectors)

    #compare scalar triple product of 3 vectors
    if scalar_tp==0:
        print("On the same plane")
    else:
        print("Not on the same plane")
    


def get_scalar_triple_product(vectors):
    '''find scalar triple product for given 3 vectors'''
    p,q,r = vectors

    cross_product = get_cross_prod(q,r)
    dot_product = get_dot_prod(p,cross_product)

    return dot_product


def get_dot_prod(p,q):
    '''return dot product of given two vectors'''
    a,b,c = p
    d,e,f = q

    dot_product = a*d+b*e+c*f

    return dot_product
    
def get_cross_prod(p,q):
    '''return cross product of given two vectors'''
    a,b,c = p
    d,e,f = q

    #find cross product vector
    cross_product = [b*f-c*e,c*d-a*f,a*e-b*d]

    return cross_product


def get_vectors(points):
    '''return vectors for given points with respective first point'''
    vectors = []
    for point in points[1:]:
        vector = []
        for a,b in zip(point,points[0]):
            vector.append(a-b)
        vectors.append(vector)

    return vectors

            
def get_points(n):
    '''get points from user return as integer lists'''
    points = []
    for i in range(n):
        point = list(map(int,input().strip().split()))
        points.append(point)

    return points

main()
