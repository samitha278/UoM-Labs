#Solution by Bandara M.A.G.S.S

#Riemann Integration

#calculating riemann midpoint sum

'''
case 1;
input:  1 2 3
        3 4
        100
output: 45.00

case 2;
input:  1 0 2 0 5
        10 20
        200
output: 3104662.08
'''


def main():
    '''main function'''
    coefficients = get_coefficient()
    if coefficients==-1:
        return -1

    interval = get_interval()
    if interval==-1:
        return -1

    n = get_integer()
    if n=="z":
        return -1

    sub_length = get_sub_length(n,interval)

    partitions = get_partitions(n,sub_length,interval)

    function = get_function(coefficients)

    midpoint_riemann_sum = get_midpoint_riemann_sum(n,sub_length,partitions,function)

    print("%.2f"%midpoint_riemann_sum)



def get_midpoint_riemann_sum(n,sub_length,partitions,function):

    riemann_sum = []

    for i in range(n):
        p = partitions[i]    
        q = partitions[i+1]

        x = (p+q)/2
        y = y_value(x,function)

        riemann_sum.append(y*sub_length)
        

    return sum(riemann_sum)
    

def y_value(x,function):
    y = 0

    for expo,coeff in function.items():
        y+= coeff *(x**expo)

    return y         


def get_function(coefficients):
    function = {}

    n = 0
    for co in coefficients:
        function[n] = co
        n+=1

    return function

#print(y_value(1,get_function([1,2,3])))


def get_partitions(n,sub_length,interval):

    a,b = interval
    dx = sub_length

    s = len(str(sub_length))

    partitions = [a+(dx*i) for i in range(n)]+[b]

    return partitions


#print(get_partitions(100,0.01,[3,4]))


def get_sub_length(n,interval):
    a,b = interval

    dx = (b-a)/n

    return dx

#print(get_sub_length(100,[3,4]))

  
def get_integer():
    try:
        integer = int(input().strip())
    except:
        return "z"

    return integer

#print(get_integer())    
     
def get_interval():
    try:
        interval = list(map(int,input().strip().split()))
    except:
        return -1
    
    a,b = interval

    if a<b:
        return interval

    return -1

#print(get_interval())

def get_coefficient():
    try:
        coefficients = list(map(int,input().strip().split()))
    except:
        return -1
    
    return coefficients

#print(get_coefficient())


#drver code
if __name__=='__main__':
    main()
