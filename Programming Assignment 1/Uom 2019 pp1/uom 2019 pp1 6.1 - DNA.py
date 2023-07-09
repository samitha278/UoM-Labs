#Solution by Bandara M.A.G.S.S

#DNA

def main():
    dna_parent = get_dna()

    dna_child = get_dna()
    if len(dna_parent)!=len(dna_child):
        return -1

    score = dna_score2(dna_parent,dna_child)

    print(score)
    return 0

def dna_score(dna_p,dna_c):

    comp = {'A':'T','C':'G','G':'C','T':'A'}
    
    score = 0
    for i,c in enumerate(dna_c):
        if c != dna_p[i]:
            if c=='_':
                score+=6
            elif c==comp[dna_p[i]]:
                score+=2
            else:
                score+=4

    return score

def dna_score2(dna_p,dna_c):
    comp = {'A':'T','C':'G','G':'C','T':'A'}

    comp_p = [comp[c] for c in dna_p]

    score = sum([6 if c=='_' else 2 if c==cp else 4 for c,p,cp in zip(dna_c,dna_p,comp_p) if c!=p])

    return score

def get_dna():
    while True:
        inp = input().strip()
        dna = [c for c in inp]

        char = ['A','C','G','T','_']

        if all((c in char for c in dna)):
            break
    return dna


if __name__=="__main__":
    main()
