#Solution by Bandara M.A.G.S.S

#Hamming Numbers

def main():
    '''main function'''
    ran = get_range()

    sum_ham = sum(hamming_nums(ran))

    print(sum_ham)

    return 0


def hamming_nums(ran):
    '''return hamming number list to given range'''
    p,q = ran

    ham_nums = []
    for i in range(p,q+1):
        if isHamming2(i):         #check number is hamming or not
            ham_nums.append(i)     #if number is hamming number add to list

    return ham_nums

def isHamming1(n):
    '''find given number is hamming number using loop'''
    temp = n

    ham_digits = [1,2,3,4,5,6,8,9]
    while True:
        if temp in ham_digits:
            return True
        elif temp%2==0:
            temp//= 2
        elif temp%3==0:
            temp//= 3
        elif temp%5==0:
            temp//= 5
        else:
            return False

def isHamming2(n):
    '''find given number is hamming number using recursion'''
    ham_digits = [1,2,3,4,5,6,8,9]
    if n in ham_digits:              #base case
        return True
    
    for i in [2,3,5]:
        if n%i==0:
            return isHamming2(n//i)  #recursive case
    else:
        return False
                    
def get_range():
    '''get range from user'''
    while True:                    #looping untill user give correct range
        inp = input().strip()      #get input as string
        if int == "":
            continue
        try:
            inp_lst = list(map(int,inp.split()))    #convert string list to integer list
        except:
            continue
        else:
            return inp_lst


if __name__=='__main__':
    main()
        
