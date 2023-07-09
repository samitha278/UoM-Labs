#Solution by Bandara M.A.G.S.S

#Grade point average


def main():
    num_of_subjects,num_of_rows = n,m = list(map(int,input().split()))

    grades = input().split()

    weights = list(map(int,input().split()))

    if len(grades)!=n and len(wights)!=n:
        print("Invalid Input")

    grading_schema = {} 
    for _ in range(m):
        grade,point = input().split()

        grading_schema[grade] = float(point)

    
    gpa = calculate_gpa(n,grading_schema,grades,weights)

    rounds = [i-gpa if (i-gpa)>=0 else gpa-i for i in grading_schema.values()]
    average_grade = list(grading_schema.keys())[rounds.index(min(rounds))]
        
    print("%.2f"%gpa)
    print(average_grade)

def calculate_gpa(n,grading_schema,grades,weights):
    numerator = sum(grading_schema[grades[i]]*weights[i] for i in range(n))
    denominator = sum(weights)

    gpa = numerator/denominator

    return gpa

main()
