#Solution by Bandara M.A.G.S.S

#Text formatter

def main():
    n = get_pint()
    lines = get_lines(n)

    print_lines(n,lines)

def print_lines(n,lines):
    
    i = 0
    while i!=n:
        fomt = lines[i][0]
        counter = 1
        while fomt=="ol": 
            print_line(["ol",f"{counter}. {lines[i][1]}"])
            i+=1
            counter += 1
            if i!=n:
                fomt = lines[i][0]
            else:
                break
        else:
            print_line(lines[i])
            i+=1


def print_line(line):
        fomt = line[0]
        text = line[1]
        l = len(text)
        
        match fomt:
            case "h1":
                print("//"+"="*(l+2)+"\\"+"\\")
                print("|| "+ text.upper() +" ||")
                print("\\"+"\\"+"="*(l+2)+"//")
            case "h2":
                print(" "+text+" ")
                print("-"*(l+2))
            case "ol":
                print(text)
            case "ul":
                print("> "+text)
            case "pp":
                print(text)
            case _:
                return -2
    
def get_lines(n):

    line_lst = []
    for i in range(n):
        while True:
            line = input().strip().split(" ",1)
            if len(line)==2:
                break
            else:
                print(f"missing {line[0]} , try again!")
        line_lst.append(line)

    return line_lst

def get_pint():
    while True:
        inp = input().strip()
        try:
            n = int(inp)
        except:
            continue

        if n<0:
            continue
        else:
            return n

if __name__=='__main__':
    main()
