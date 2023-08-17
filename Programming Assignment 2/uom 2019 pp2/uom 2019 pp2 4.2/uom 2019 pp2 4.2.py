def main():

    file_path = input().strip()

    matrix = read_file(file_path)
    if matrix == -1: return -1

    maximum_adj_sum = get_maximum_adj_sum(matrix)

    print(maximum_adj_sum)

    if write_file("F:\\uom 2019 pp2\\uom 2019 pp2 4\\output 4.2.txt",maximum_adj_sum)==-1:return -1

    
def write_file(file_path,output):
    '''
    write output to file
    '''
    
    try:
        with open(file_path,"w") as file:
            file.write(str(output)+'\n')     
    except Exception as e:
        print("Error!",e)
        return -1

    return 0
    

def get_maximum_adj_sum(matrix):

    rows,columns = len(matrix),len(matrix[0])

    max_sum_rows = max(sum(row) for row in matrix)

    max_sum_columns = max(
        sum([matrix[j][i] for j in range(rows)])
        for i in range(columns)
        )

    return max([max_sum_rows,max_sum_columns])



def read_file(file_path):

    try:
        with open(file_path,"r") as file:
            n = int(file.readline())

            if n<2:return -1

            matrix = [
                list(map(int,file.readline().rstrip().split()))
                for i in range(n)
                ]
            
    except Exception as e:
        print("Error!",e)
        return -1

    return matrix

#read_file function checker
#print(read_file("F:\\uom 2019 pp2\\uom 2019 pp2 4\\input 4.2.txt"))

main()
