def main():

    file_location = input()  #F:\\uom 2019 pp2\\uom 2019 pp2 11\\input 11.2.txt

    numbers = read_file(file_location)
    if numbers == -1:return -1

    validity = check_validity(numbers)
    if validity == -1:return -1

    writer = write_file(validity)
    if writer == -1:return -1
    


def read_file(file_location):
    
    numbers = []

    try:
        with open(file_location ,'r') as file:
            n = int(file.readline())
            for i in range(n):
                number = file.readline()
                if '\n' in number:
                    numbers.append(number[:-1])
                else:
                    numbers.append(number)
    except:
        print("Error")
        return -1        

    return numbers




def check_validity(numbers):
    n = len(numbers)
    if n==0:return -1
            
    validity = []

    for number in numbers:
        if int(number[0]) not in [4,5,6]:
            validity.append("Invalid\n")
            continue
        
        if "-" in number:
            alist = number.split("-")
            if any(len(part)!=4 for part in alist):
                validity.append("Invalid\n")
                continue
            number = "".join(alist)
        

        if len(number)!= 16 or any(not n.isdigit() for n in number):
                validity.append("Invalid\n")
                continue

        
        if isConcecetive(number):
            validity.append("Invalid 4\n")
            continue
        

        validity.append("Valid\n")

    return validity



def isConcecetive(number):


    '''
        count = 0
        while count<15:
            n = number[count]
            count += 1
            
            counter = 1
            while count<15 and number[count]==n:
                counter += 1
                
                count += 1
                

            if counter>3:
                validity.append("Invalid\n")
                continue

        '''

    ################################################################
    length = len(number)
    for i in range(length):
        if number.count(number[i],i,i+4) > 3:
            return True
        ###############################################################
        
    return False
            


def write_file(alist):

    try:
        with open("F:\\uom 2019 pp2\\uom 2019 pp2 11\\output 11.2.txt" ,'w') as file:
            for c in alist:
                file.write(c)
    except FileNotFoundError as e:
        print(e)
        return -1

    return 0
        
            

main()
