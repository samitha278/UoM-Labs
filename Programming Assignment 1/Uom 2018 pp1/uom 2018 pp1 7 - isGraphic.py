#Solution by Bandara M.A.G.S.S

#isGraphic

def main():
    sequence = get_sequence()

    if isGraphic(sequence):
        print("Graphic")
    else:
        print("Non-Graphic")


def isGraphic(sequence):
    
    total_value = sum(sequence)
    
    condition1 = total_value%2==0
    
    condition2 = cond_2(sequence)

    return condition1 and condition2

        
def cond_2(sequence):
    
    n = len(sequence)

    for k in range(n):
        
        a = sum(sequence[i] for i in range(k))

        b = k*(k-1) + sum(min([sequence[i],k]) for i in range(k,n))

        if a>b:
            return False

    return True
        
     
def get_sequence():
    ''''input sequence from user and return sequence
        otherwise if error raised function run recursively '''
    try:
        sequence = list(map(int,input().strip().split(",")))
        return sequence 
    except:
        print("invalid input")
        return get_sequence()

    
    
main() 
    
