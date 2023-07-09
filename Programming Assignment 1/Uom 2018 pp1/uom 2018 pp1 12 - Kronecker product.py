#Solution by Bandara M.A.G.S.S

#Kronecker product

def main():
    n = int(input().strip())

    matrix1 = get_matrix(n)
    matrix2 = get_matrix(n)

    krnecker = get_krnecker(n,matrix1,matrix2)

    print_matrix(krnecker)


def print_matrix(matrix):
    for row in matrix:
        for i in range(len(row) - 1):
            print(row[i], end=", ")
        print(row[-1])
    


def get_krnecker(n,matrix1,matrix2):
    x = n*n
    krnecker = []
    
    for row in matrix1:
        k_row = []
        for i in row:
            k_row.append(scalar_matrix_mul(i,matrix2))
        krnecker.append(k_row)

    k_matrix = []

    for i in range(n):
        for j in range(n):
            row = []
            for k in range(n):
                row.extend(krnecker[i][k][j])
            k_matrix.append(row)
        
    return k_matrix



def scalar_matrix_mul(n,matrix):
    mul_matrix = []

    for row in matrix:
        mul_row = []
        for i in row:
            mul_row.append(n*i)
        mul_matrix.append(mul_row)

    return mul_matrix       


def get_matrix(n):
    inputs = list(map(int,input().split(",")))


    matrix = []

    for i in range(n):
        row = [inputs[n*i+j] for j in range(n)]
        matrix.append(row)
    
    return matrix

main()
