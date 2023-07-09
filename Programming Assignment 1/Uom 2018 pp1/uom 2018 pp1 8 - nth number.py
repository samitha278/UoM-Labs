#Solution by Bandara M.A.G.S.S

#nth number

def main():
    integers = get_integers()

    nth_numbers = get_nth_numbers(integers)

    for i in nth_numbers:
        print(i)

    
def get_nth_numbers(integers):
    seq = {0:0,1:4}

    nth_numbers = []
    
    for n in integers:
        if n in seq:
            nth_numbers.append(seq[n])
            continue

        for i in range(2,n+1):
            if i in seq:continue
            seq[i] = ((3*(i+3)*seq[i-1])//(i+2)) - ((2*(i+3)*seq[i-2])//(i+1))

        nth_numbers.append(seq[n])

    return nth_numbers

        
def get_integers():
    integers = []
    while True:
        try:
            number = int(input().strip())
        except:
            continue

        if number<0:
            return integers
        
        integers.append(number)   

        
            
main()
