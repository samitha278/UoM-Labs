#Solution by Bandara M.A.G.S.S

#Bouncy numbers


def main():
    '''main function'''
    ran = get_range()   #get range from user

    b_sum = bouncy_sum(ran)     #calculate sum of bgouncy numbers given range

    print(b_sum)            #print sum of bouncy numbers 

    return 0


def bouncy_sum(ran):

    '''return sum of bouncy numbers to given range'''
    p,q = ran
    
    b_sum = 0
    for i in range(p,q+1):           #iterate through given range
        if i<100:
            continue
        elif isincre(i) or isdecre(i):    #check number is increse number or decrease number
            continue
        else:
            b_sum += i          #adding bouncy numbers

    return b_sum
    

def isdecre(n):
    '''return True if number is decresing number otherwise False'''
    n_str_lst = [char for char in str(n)]    #convert integer to list of chars

    n_lst = list(map(int,n_str_lst))        #convert string list to integer list
    
    for index,i in enumerate(n_lst):
        try:
            if i<n_lst[index+1]:        #check number decrease or not
                return False
        except:
            break
            
    return True

def isincre(n):
    '''return True if number is incresing number otherwise False'''

    n_str_lst = [char for char in str(n)]     #convert integer to list of chars

    n_lst = list(map(int,n_str_lst))         #convert string list to integer list
    
    for index,i in enumerate(n_lst):        #check number increase or not
        try:
            if i>n_lst[index+1]:
                return False
        except:
            break

    return True
            
        
def get_range():
    '''get range from user'''
    while True:
        ran_str = input().strip()

        try:
            ran = list(map(int,ran_str.split()))
        except:
            continue
        else:
            return ran


if __name__ == '__main__':
    main()

