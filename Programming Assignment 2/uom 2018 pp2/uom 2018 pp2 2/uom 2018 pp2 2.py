def main():

    try:
        with open(input().strip()) as file:
            n = int(file.readline().rstrip())
    except:
        return -1

    if not -127<=n<=127:
        return -1
    
    twosCom = getTowsCom(n)

    print(twosCom)



def getTowsCom(n):

    binVal = binary_8bit(abs(n))

    invert = "".join(["0" if int(bit) else "1" for bit in binVal] )

    addOne = int(invert,2)+1

    return binary_8bit(addOne)
    





def binary_8bit(n):

    binary_rev = []

    temp = n
    
    while temp!=1:
        binary_rev.append(str(temp%2))
        temp//=2
    else:
        binary_rev.append(str(temp))

    balance = 8-len(binary_rev)
    bin_8bit = ["0"]*balance + binary_rev[::-1]
    
    bin_8bit_str = "".join(bin_8bit)

    return bin_8bit_str
    





main()
