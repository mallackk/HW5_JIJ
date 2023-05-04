import csv

def main():
    f = open('202303_Seoul_Subway.csv', 'r', encoding='cp949')
    data = csv.reader(f)
    header = next(data)

    lines = ["1호선", "2호선", "3호선", "4호선"]
    bsn = ['', '', '', '']
    lsn = ['', '', '', '']
    bs = [-0x7FFFFFFFFFFFFFFF, -0x7FFFFFFFFFFFFFFF, -0x7FFFFFFFFFFFFFFF, -0x7FFFFFFFFFFFFFFF]
    ls = [0x7FFFFFFFFFFFFFFF, 0x7FFFFFFFFFFFFFFF, 0x7FFFFFFFFFFFFFFF, 0x7FFFFFFFFFFFFFFF]

    for row in data:
        flag = False
        flag2 = False
        for scan in row:
            if scan == '':
                flag = True
        for line in lines:
           if line == row[1]:
               flag2 = True
        if flag2 == False:
            flag = True

        row[4] = int(row[4])
        row[5] = int(row[5])

        if flag == False:
            tmp = int(row[1].replace('호선', ''))-1
            if row[4]+row[5] > bs[tmp]:
                bs[tmp] = row[4]+row[5]
                bsn[tmp] = row[3]
            if row[4]+row[5] < ls[tmp]:
                ls[tmp] = row[4]+row[5]
                lsn[tmp] = row[3]

    print('*** Subway Report for Seoul on March 2023 ***')
    for i in range(4):
        print(f'line {i+1}:')
        print(f'Busiest Station: {bsn[i]} ({bs[i]})')
        print(f'Least used Station: {lsn[i]} ({ls[i]})')


    f.close()

if __name__ =="__main__":
    main()
    