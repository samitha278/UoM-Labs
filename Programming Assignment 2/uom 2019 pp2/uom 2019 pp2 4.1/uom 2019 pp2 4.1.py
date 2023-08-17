def main():

    file = input().strip()

    fractions = read_file(file)
    if fractions == -1: return -1

    print(fractions)

    output = add_fractions(fractions)

    print(output)
    
    
    if write_file("C:\\Users\\apkal\\OneDrive\\Desktop\\New folder\\output 4.2.txt",output) == -1 :
        return -1

    
def write_file(file,output):
    try:
        with open(file,"w") as file:
            file.write(output+'\n')
    except:
        print("error while writing file")
        return -1

    return 0

def add_fractions(fractions):

    fraction_list = [tuple(map(int,fra.split('/'))) for fra in fractions] 
    denominators = [tup[0] for tup in fraction_list] 
    numerator = [tup[1] for tup in fraction_list]

    numes_lcm = lcm(numerator)
    
    ans_deno = sum(n*(numes_lcm//numerator[i]) for i,n in  enumerate(denominators))
    
    ans = ans_deno/numes_lcm
    str_ans = str(ans).split('.')
    if int(str_ans[-1]) == 0:
        return str_ans[0]
    
    k = gcd([ans_deno,numes_lcm])
    
    if k==1:
        return f"{ans_deno}/{numes_lcm}"
    else:
        return f"{ans_deno//k}/{numes_lcm//k}"
           

def lcm(nums):

    mul_num = 1

    for i in nums:
        mul_num *=i
        
    num_lcm = mul_num//gcd(nums)

    return num_lcm


def gcd(nums):

    facs_lst = [set(get_factors(i)) for i in nums]

    
    inter_set = facs_lst[0]
    for fac in facs_lst[1:]:
        inter_set = inter_set.intersection(fac)

    if len(inter_set)==0:
        return 1

    lcm_num = max(inter_set)
    
    
    return lcm_num



'''
def gcd2(a,b):
    while b!=0:
        t = b
        b = a%b
        a = t
    return a
'''


def get_factors(n):
    return [ i for i in range(1,n+1) if n%i==0]
    
 

def read_file(file):
    try:
        with open(file,"r") as file:
            n = int(file.readline())
            data = [file.readline().rstrip()  for _ in range(n)]

    except:
        print("error while opening file")
        return -1
    
    return data
            
    

main()
