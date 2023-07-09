#Solution by Bandara M.A.G.S.S

#Hits & Pseudohits

import random

def main():
    """main function"""

    sol = genarate_sol()
    gusses = get_gusses()

    hits = get_hits(sol,gusses)

    print(sol)
    print_hits(hits)

    return 0

def print_hits(alist):
    for tup in alist:
        print(tup,end=" ")

    return 0

def get_hits(sol,gusses):

    lst_tup = []
    
    for guss in gusses:
        hits = 0
        pseudo_hits = 0

        #calculate hits
        
        hit_index = []
        for i in range(4):
            if guss[i] == sol[i]:
                hits+=1
                hit_index.append(i)

        n = len(hit_index) 
        if n==4:
            continue

        #calculate pseudo_hits
        
        temp_g = []
        temp_s = []
        for i in range(4):
            if i not in hit_index:
                temp_g.append(guss[i])
                temp_s.append(sol[i])

        for char in temp_g:
            if char in temp_s:
                pseudo_hits += 1

        lst_tup.append((hits,pseudo_hits))

    return lst_tup        


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
    alst = ['R','Y','G','B']

    rand_lst = []
    for i in range(4):
        rand_lst.append(random.randint(0,3))

    sol = ""
    for i in rand_lst:
        sol+= alst[i]
        
    return sol


if __name__ == '__main__':
    main()
    
