#Solution by Bandara M.A.G.S.S

#Permutations

def main():
    n = get_int()

    lst = get_list()

    permu = permutation(lst)
    print(len(permu))
    print(permu[0],permu[n],permu[-1])

    return 0


def permutation(lst):

    #base case
    if len(lst)==1:
        return lst[0]
    if len(lst)==2:
        return [lst[0]+lst[1],lst[1]+lst[0]]

    permu_lst = []
    
    
    for i in lst:
        fix = i

        temp_lst = lst[:]
        temp_lst.remove(i)

        #recursive case
        permu = permutation(temp_lst)

        for j in permu:
            permu_lst.append(fix+j)

    return permu_lst
    
def get_list():
    while True:
        str_lst = input().strip()
        if str_lst!= "":
            break
        
    lst = str_lst.split()

    return lst
    

def get_int():
    while True:
        try:
            n = int(input().strip())
        except:
            continue
        else:
            break

    return n


#driver code
if __name__ == '__main__':
    main()
