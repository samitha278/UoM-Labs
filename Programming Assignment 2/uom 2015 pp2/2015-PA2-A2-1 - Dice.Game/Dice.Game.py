def main():

    try:
        with open(input().strip()) as file:
            x,y = list(map(int,file.readline().rstrip().split()))
    except Exception as e:
        print(e)
        return -1

    results = getDiceResult(x,y)

    print(results)


def getDiceResult(x,y):

    way1=way2=way3=0

    for i in range(1,7):
        xdiff = abs(i-x)
        ydiff = abs(i-y)

        if xdiff < ydiff:
            way1 += 1
        elif xdiff > ydiff:
            way3 += 1
        else:
            way2 += 1
            


    return (way1,way2,way3)



main()
