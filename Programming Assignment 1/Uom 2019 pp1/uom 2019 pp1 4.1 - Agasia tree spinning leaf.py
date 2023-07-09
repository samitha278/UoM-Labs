#Solution by Bandara M.A.G.S.S

#Agasia tree spining leaf


def main():
    seconds = int(input().strip())

    height = find_height(seconds)

    print(height)

def find_height(time):
    '''return distance fell down by the leaf in meters using given time '''

    '''#create list that contain first nth fibonacci numbers 
    fibonacci_numbers = [fibonacci(i) for i in range(1,time+1)]

    #find height by using first nth fibonacci numbers
    height= sum(i**0.5 for i in fibonacci_numbers)'''

    height= sum(i**0.5 for i in n_fibonaccis(time))

    return round(height,3)


def fibonacci(n):
    '''return nth fibonacci number using recursion'''
    #base case
    if n==1 or n==2:
        return 1

    #recursive case
    return fibonacci(n-1)+fibonacci(n-2)





def n_fibonaccis(n):
    fibonacci = {}

    fibonacci[1] = fibonacci[2] = 1

    for i in range(3,n+1):
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]

    return list(fibonacci.values())


if __name__=="__main__":
    main()
