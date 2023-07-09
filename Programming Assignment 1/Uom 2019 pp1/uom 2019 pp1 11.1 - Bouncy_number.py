#Solution by Bandara M.A.G.S.S

#Bouncy numbers


def main2():
    ran = get_range2()
    bouncy_sum_value = bouncy_sum2(ran)
    print(bouncy_sum_value)
    return 0


def bouncy_sum2(ran):
    p, q = ran
    b_sum = 0
    for i in range(p, q + 1):
        if i < 100 or is_bouncy(i):
            b_sum += i
    return b_sum


def is_bouncy(n):
    digits = [int(digit) for digit in str(n)]
    increasing = all(digits[i] <= digits[i+1] for i in range(len(digits)-1))
    decreasing = all(digits[i] >= digits[i+1] for i in range(len(digits)-1))
    return not (increasing or decreasing)


def get_range2():
    ran_str = input().strip()
    ran = list(map(int, ran_str.split()))
    return ran


if __name__ == '__main__':
    main2()

