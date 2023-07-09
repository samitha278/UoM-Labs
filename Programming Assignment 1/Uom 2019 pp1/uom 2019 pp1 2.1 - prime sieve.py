#Solution by Bandara M.A.G.S.S

#Prime sieve

def main():
    """main function"""
    while True:
        try:
            lim = int(input())
            break
        except ValueError:
            continue
        
    grid = create_grid(lim)

    print_grid(grid,lim)
    print_primes(grid)

    return 0



def create_grid(n):
    grid = {}

    for i in range(1,n+1):
        grid[i] = "O"

    keys =list(grid.keys())
    
    grid[1] = "X"

    val_lst = list(grid.values())[1:]
    value = val_lst.count("O")

    i = 2
    
    while value !=0 :
        if grid[i] == "O":
            if i == 2:
                for j in range(3,n+1):
                    if j%2==0:
                        grid[j]="X"
            elif i == 3:
                for k in range(4,n+1):
                    if k%3==0:
                        if grid[k] == "O":
                            grid[k]="X"
                        else:
                            continue
            else:
                x = i
                for m in range(x+1,n+1):
                    if m%x==0:
                        if grid[m] == "O":
                            grid[m]="X"
                        else:
                            continue
            i+=1
            val_lst = list(grid.values())[i:]
            value = val_lst.count("O")
        else:
            i+=1

    return grid

def print_primes(dic):
    for i in dic:
        if dic[i]=="O":
            print(i,end=" ")
    print()

    return 0

def print_grid(dic,n):

    sqrt = int(n**0.5)

    alst = list(dic.keys())
    
    for i in alst[:-1]:
        if i%(sqrt+1)==0:
            print()
        print(f"{i}  :  {dic[i]}", end=" , ")

    print(f"{alst[-1]}  :  {dic[alst[-1]]}  ")
    return 0


#driver code
if __name__ == '__main__':
    main()
