#Solution by Bandara M.A.G.S.S

#Newman convey sequence

def main():
    n = int(input().strip())

    nth_term = find_nth_term(n)

    print(nth_term)



def find_nth_term(n):
    seq = [0]*(n+1)

    seq[1] = seq[2] = 1

    for i in range(3,n+1):
        seq[i] = seq[seq[i-1]] + seq[i-seq[i-1]]


    return seq[n]

main()
