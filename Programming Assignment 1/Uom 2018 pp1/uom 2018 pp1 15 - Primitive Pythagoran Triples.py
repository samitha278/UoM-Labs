#Solution by Bandara M.A.G.S.S

#Primitive Pythagoran Triples

def main():
    n = int(input().strip())

    pythogoron_triples = count_pytriples(n)

    print(pythogoron_triples)


def count_pytriples(n):
    py_triples = []
    
    for c in range(n):
        for b in range(c):
           for a in range(b):
               if c**2 == b**2 + a**2 and have_common_divisor([a,b,c]):
                    py_triples.append([a,b,c])
                   
    return len(py_triples)

def have_common_divisor(alist):
    a,b,c = alist
    for i in range(2,a):
        if a%i==0 and b%i==0 and c%i==0:
            return False

    return True
            
main()
