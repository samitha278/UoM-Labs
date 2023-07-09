#Solution by Bandara M.A.G.S.S

#3 Super number

def main():
    inputs = get_ints()

    if any(i<0 for i in inputs):return -1
    
    k,m,n = inputs

    '''nums = get_replace_nums(m,n)

    if all(num%(2**k)==0 for num in nums):
        print("True")
    else:
        print("False")'''
    
    if all(num%(2**k)==0 for num in get_replace_nums2(m,n)):
        print("True")
    else:
        print("False")

        
################################       
def get_replace_nums2(m,n):

    n_lst = [c for c in str(n)]
    length = len(n_lst)

    temp=n_lst
    for i in range(length+1):
        temp.insert(i,str(m))
        yield int("".join(temp))
        temp=n_lst
################################


def get_replace_nums(m,n):
    replace_nums = []

    n_lst = [c for c in str(n)]
    length = len(n_lst)

    temp=n_lst
    for i in range(length+1):
        temp.insert(i,str(m))
        replace_nums.append(temp)
        temp=n_lst

    nums = [int("".join(lst)) for lst in replace_nums]      

    return nums
        
    
def get_ints():
    try:
        inputs = list(map(int,input().strip().split()))
    except:
        get_ints()
    else:
        return inputs
        
main()
