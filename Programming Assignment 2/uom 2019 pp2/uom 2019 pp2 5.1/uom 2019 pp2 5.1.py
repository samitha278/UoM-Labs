def main(inpFile):

    data = read_file(inpFile)
    if data == -1: return -1

    result = sum(get_coordinates_values(data["matrix"],data["coordinates"]))

    if write_file("F:\\uom 2019 pp2\\uom 2019 pp2 5\\output 5.1.txt",result)==-1:return -1





def write_file(outFile,output):

    try:
        with open(outFile,'w') as file:
            file.write(f"{output}\n")
    except Exception as e:
        print(f"Error! {e}")
        return -1

    return 0
    
    

def get_coordinates_values(matrix,coordinates):

    matrix_values = [matrix[coo[1]-1][coo[0]-1] for coo in coordinates]

    #print(matrix_values) #debugger 5

    return matrix_values



def read_file(inpFile):

    try:
        with open(inpFile) as file:
            #read dimention
            columns,rows = list(map(int,(file.readline().rstrip() for i in range(2))))

            #print(columns,rows) #debugger 1
            
            #read matrix
            matrix = [
                list(map(int,file.readline().rstrip().split()))
                for i in range(rows)
            ]
            
            if any(len(row)!=columns for row in matrix):raise Exception
            
            #print(matrix) #debugger 2

            #read coordinates
            coordinates = []
            while (temp:=file.readline())!="":
                coordinates.append(coo:=tuple(map(int,temp.rstrip().split())))

                #print(temp,coo) #debugger 3
            

    except Exception as e:
        print(f"Error! {e}")
        return -1
    
    data = {
        "matrix":matrix,
        "coordinates":coordinates
    }

    #print(data)  #degugger 4
    
    return data



if __name__=="__main__":
    main(input("file path: ").strip())  #F:\\uom 2019 pp2\\uom 2019 pp2 5\\input 5.1.txt
