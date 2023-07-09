#Solution by Bandara M.A.G.S.S

#matrix Multiply

def main():
    while True:
        r1,c1 = get_rc()
        mat1 = get_matrix(r1,c1)

        r2,c2 = get_rc()
        mat2 = get_matrix(r2,c2)

        if c1!=r2:
            print("Invalid Input")

        mat_mul = mat_multiplier(mat1,mat2)

        print_matrix(mat_mul)

        yn = input("wanna try again? (y/n): ")
        if yn=="n":
            print("come again!")
            break
    
def print_matrix(matrix):
    r,c = len(matrix),len(matrix[0])

    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end=" ")
        print()

        
    
def mat_multiplier(mat1,mat2):
    r1,c1 = len(mat1),len(mat1[0])
    r2,c2 = len(mat2),len(mat2[0])

    mul_matrix = [] 
    for i in range(r1):
        row = []
        for j in range(c2):
            ele = 0
            for k in range(c1):
                ele += mat1[i][k]*mat2[k][j]
            row.append(ele)
        mul_matrix.append(row)

    return mul_matrix
    

def get_matrix(rows,columns):
    matrix = []
    print("Enter matrix: ")
    for i in range(rows):
        row_str = input().strip().split()
        try:
            row = list(map(int,row_str))
        except:
            return -2

        if len(row)==columns:
            matrix.append(row)
        else:
            return -2

    return matrix

    
def get_rc():
    while True:
        inp = input("Enter rows & columns: ").strip()

        if inp == "":
            continue
        
        try:
            inp_lst = list(map(int,inp.split()))
        except:
            continue
        else:
            return inp_lst
        
if __name__=='__main__':
    main()
