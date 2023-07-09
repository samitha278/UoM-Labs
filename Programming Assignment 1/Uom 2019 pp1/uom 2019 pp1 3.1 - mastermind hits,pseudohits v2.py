#Solution by Bandara M.A.G.S.S

#Hits & Pseudohits

import random

def main():

    sol = genarate_sol()
    gusses = get_gusses()

    hits = get_hits(sol,gusses)

    print(sol)
    print_hits(hits)


def print_hits(alist):
    for tup in alist:
        print(tup,end=" ")


def get_hits(sol,gusses):

    hits_list = []
    
    for guss in gusses:
        pseudo_hits = 0

        #calculate hits
        hits = sum(1 for s,g in zip(sol,guss) if s==g)

        #calculate pseudo_hits
        pseudo_hits = sum( min(guss.count(c),sol.count(c)) for c in set(guss)) - hits

        hits_list.append((hits,pseudo_hits))

    return hits_list        


def get_gusses():
    while True:
        inp_str = input().strip().upper()
        inp_lst = inp_str.split(" ")

        len_lst = [len(g) for g in inp_lst]
        
        if min(len_lst) == 4 and max(len_lst)==4:
            break
        print("Invalid input!!")

    return inp_lst


def genarate_sol():
    colors = ['R','Y','G','B']
    random.shuffle(colors)
    return "".join(colors)


#driver code
if __name__ == '__main__':
    main()
    
