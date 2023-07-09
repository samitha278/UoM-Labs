#Solution by Bandara M.A.G.S.S

#Look and say

def main():
    m = int(input().strip())
    n = int(input().strip())

    nth_number = create_sequence(m,n)

    print(nth_number)


def create_sequence(m,n):
    seq = {}
    
    seq[1] = m

    for i in range(2,n+1):
        seq[i] = get_next_value(seq[i-1])

    print(seq)

    return seq[n]

def get_next_value(n):

    num_str = str(n)
    l = len(num_str)
    next_val = ""

    if len(num_str)==1:
        return int("1"+str(n))

    
    count = 0
    while count<l:
        char = num_str[count]
        count+=1
        num_count = 1
        while count<l and char == num_str[count]:
            count+=1
            num_count+=1
        

        next_val+=str(num_count)+char

    return int(next_val)
            
            
            


main()
        
    
