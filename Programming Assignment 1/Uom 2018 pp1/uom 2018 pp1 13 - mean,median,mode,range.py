#Solution by Bandara M.A.G.S.S

#mean,median,mode,range

def main():
    seq = list(i for i in map(int,input().strip().split()) if i!=-1 )

    #find mean
    length = len(seq)
    mean = sum(seq)/length
    print(f"mean: %.2f"%mean)

    #find median
    sorted_seq = sort_seq(seq)
    median = sorted_seq[length//2]
    print("medain:",median)

    #find_mode
    mode = find_mode2(seq)
    print("mode: ",end="")
    for i in mode[:-1]:
        print(i,end=",")
    print(mode[-1])

    #find range
    seq_range = max(seq) - min(seq)
    print("range:",seq_range)

    

'''def find_mode(seq):
    set_seq = list(set(seq))
    
    counts = [seq.count(i) for i in set_seq]

    return set_seq[counts.index(max(counts))]'''



def find_mode2(seq):
    dic = {}

    for i in seq:
        if i not in dic:
            dic[i] = seq.count(i)

    max_count = max(dic.values())

    ##################################################################
    mode_list = [key for key,value in dic.items() if max_count==value]
    ##################################################################

    return mode_list
    
    
#print(find_mode2([2,1,6,3,9,2,0,2,4,8]))

def sort_seq(seq):
    sorted_seq = []

    temp = seq[:]
    for i in range(len(seq)):
        minimum = min(temp)
        sorted_seq.append(minimum)
        temp.remove(minimum)

    return sorted_seq


#print(sort_seq([2,1,6,3,9,2,0,2,4,8]))       

main()

    
