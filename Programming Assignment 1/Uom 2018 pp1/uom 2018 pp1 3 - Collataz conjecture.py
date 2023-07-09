#Solution by Bandara M.A.G.S.S

#Collataz conjecture


def main():
    initial_range = get_range()
    if initial_range == -1: return -1

    p,q = initial_range
    
    detail_tuple = collatz_conjecture(p,q)
    max_time,max_max = detail_tuple

    print(max_time)
    print(max_max)
    

#using dynamic programming
def collatz_conjecture(p,q):
    base_collatz = [16,8,4,2,1]

    collatz_cache = {16:base_collatz}

    total_times = []
    maximums = []

    for n in range(p,q+1):
        if n == 0:
            continue
        
        collatz_seq = []
        temp = n

        if n==1:collatz_seq.append(1)

        while temp!=1:
            z = temp
            if temp in base_collatz:
                index = base_collatz.index(temp)
                collatz_seq.extend(base_collatz[index:])
                break
            
            elif temp in collatz_cache:
                collatz_seq.extend(collatz_cache[temp])
                break
            
            elif temp%2==0:
                temp//+2
            else:
                temp = 3*temp+1

            if temp in collatz_cache:
                if (temp-1)%3 == 0:
                    x = (temp-1)//3
                    collatz_cache[x] = [x]+collatz_cache[temp]

                y = temp*2
                collatz_cache[y] = [y]+collatz_cache[temp]

                collatz_cache.pop(temp)
                    

            collatz_seq.append(z)

        
        total_times.append(len(collatz_seq)-1)
        maximums.append(max(collatz_seq))
   
    max_time = max(total_times)
    max_max = max(maximums)

    print(collatz_cache)
    
    return max_time,max_max


'''def collatz_conjecture2(p,q):
    
    total_times = []
    maximums = []

    for n in range(p,q+1):
        if n<=0:continue
        
        collatz_seq = []
        temp = n

        if n==1:collatz_seq.append(1)

        collatz_seq.append(n)
        
        while temp!=1:
            if temp%2==0:
                temp//=2
            else:
                temp= 3*temp+1

            collatz_seq.append(temp)

        total_times.append(len(collatz_seq)-1)
        maximums.append(max(collatz_seq))
    
    max_time = max(total_times)
    max_max = max(maximums)

    return max_time,max_max'''


def get_range():
    inp = input().strip()

    initial_range= n1,n2 = list(map(int,inp.split()))

    if 0<=n1<n2:
        return initial_range

    print("invalid input")
    return -1


main()
