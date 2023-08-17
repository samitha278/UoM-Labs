#Find  Levenshtein Distance

def main():
    try:
        with open(input().strip()) as file:
            words = [line.rstrip().split() for line in file]
    except Exception as e:
        print(e)
        return -1

    distances = [getLevenshteinDistance(pair[0], pair[1]) for pair in words]

    with open("output.txt", "w") as file:
        for distance in distances:
            print(distance)
            file.write(str(distance) + "\n")


def getLevenshteinDistance(word1, word2):
    m = len(word1)
    n = len(word2)

    # Create a matrix to store distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the matrix
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill in the matrix using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if word1[i - 1] == word2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

    return dp[m][n]


if __name__ == "__main__":
    main()














def main():

    try:
        with open(input().strip()) as file:
            words = [line.rstrip().split() for line in file]

    except Exception as e:
        print(e)
        return -1

    distances = [getLavDis(pair[0],pair[1]) for pair in words] 

    with open("output.txt","w") as file:
        for line in distances:
            print(line)
            file.write(str(line)+"\n")

    

def getLavDis(word1,word2):

    dis = 0

    m = len(word1)
    n = len(word2)
    l = min(n,m)

    lst = list(word1)
    word = "".join(lst)

    i=0
    
    while i<l:
        
        if word == word2:
            break

        '''
        if m<n and word == word2[:l]:
            break
        elif m>n and word[:l]==word2:
            break
        elif m==n and word==word2:
            break
        ''' 




        if i==0:
            l1 = ""
            l2 = ""
        else:
            l1 = word[i-1]
            l2 = word2[i-1]
        
        m1 = word[i]
        m2 = word2[i]

        if i==l-1:
            if m<n:
                r1 = ""
                r2 = word2[i+1]
            elif m>n:
                r1 = word[i+1]
                r2 = ""
            else:
                r1 = ""
                r2 = ""
        else:
            r1 = word[i+1]
            r2 = word2[i+1]
            




        
        if m1!=m2:

            
            if i==0:
                
                #insertion
                if m1==r2:
                    lst.insert(i,m2)
                    print("insertion start")
                    

                #deletion
                elif r1==m2:
                    lst.remove(m1)
                    print("deletion start")

                #substitution
                elif r1==r2:
                    lst[i]=m2
                    print("sub start")

                
            elif i<l-1:
                
                #insertion
                if l1==l2 and m1==r2:
                    lst.insert(i,m2)
                    print("insertion mid")
                    

                #deletion
                elif l1==l2 and r1==m2:
                    lst.remove(m1)
                    print("deletion mid")

                #substitution
                elif l1==l2 and r1==r2:
                    lst[i]=m2
                    print("sub mid")

            else:
                if m>n:
                    #deletion
                    if l1==l2 and r1==m2:
                        lst.remove(m1)
                        print("del end m>n")
                else:
                    #substitution
                    if l1==l2:
                        lst[i]=m2
                        print("sub end m<n")

            dis+=1
            print(lst)


               
        if i==l-1 and m1==m2:
            #insertion end
            if m<n:
                lst.append(r2)
                dis+=1
                print("insertion end")
                
            #deletion end
            elif m>n:
                lst = lst[:l]
                dis+=(m-n)
                print("deletion end")
            
                  
            print(lst)    
        
        
        i+=1
        word = "".join(lst)
        m = len(word)

    if m<n:
        dis+= (n-m)

    return dis



#main()
