#Solution by Bandara M.A.G.S.S

#Id Details


def main():
    id_number = input().strip()

    if len(id_number) != 9:
        print("Invalid Id Number")

    year = '19'+id_number[:2]

    gender = ""
    date_digits = int(id_number[2:5])
    temp = date_digits

    if date_digits < 500:
        gender = 'M'
    else:
        gender = 'F'
        temp -= 500

    
    year_dates  = [31,29,31,30,31,30,31,30,31,30,31,30]

    for index,i in enumerate(year_dates):
        if temp>i:
            temp-=i
        else:
            month = index+1
            date = temp
            break

    if date<10:
        date='0'+str(date)
    if month<10:
        month='0'+str(month)
        
    print(f"{year}-{month}-{date}")
    print(gender)


main()
        
