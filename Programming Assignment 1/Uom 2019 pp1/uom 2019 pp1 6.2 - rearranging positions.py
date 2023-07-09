#Solution by Bandara M.A.G.S.S

#rearranging positions

def main():
    while True:
        students = get_line()
        instructs = get_line()
        if len(students)==len(instructs):
            break
        else:
            print("invalid instructions or number of students")
        
    new_positions = rearrange(students,instructs)

    np_str = "_".join(new_positions) 
    print(np_str)



def rearrange(students,instructs):
    temp = students[:]

    for s,inst in zip(students,instructs):
        i1,i2 = inst[0],int(inst[1])

        if i1=="R":
            posi = temp.index(s)+i2
        else:
            posi = temp.index(s)-i2

        temp.remove(s)
        temp.insert(posi,s)

    new_positions = [f"{temp.index(s)+1}" for s in students]       
    
    return new_positions


def get_line():
    inp = input().strip().split('_')
    return inp


main()
