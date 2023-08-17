def main():

    with open(input().strip()) as file:
        texts = [line.rstrip().split() for line in file]


    for word1,word2 in texts:
        if isAnagram(word1,word2):
            print("Anagram")
        else:
            print("Not Anagram")


def isAnagram(word1,word2):

    t1,t2 = word1,word2

    if sorted(t1)==sorted(t2):
        return True

    return False
    







main()
