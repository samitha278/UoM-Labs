#Solution by Bandara M.A.G.S.S

#isPermutation

def main():
    n = int(input().strip())

    matrix = get_matrix(n)

    if isPermutation(n,matrix):
        print("YES")
    else:
        print("NO")


def isPermutation(n,matrix):

    for row in matrix:
        if row.count(1)!=1 or row.count(0)!=n-1:
            return False

    return True
            


def get_matrix(n):

    mat_list = list(map(int,input().strip().split(",")))
    if len(mat_list)!=n*n:
        print("invalid input")
        return get_matrix(n)

    matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(mat_list[n*i+j])
        matrix.append(row)

    return matrix
            

main()    

