import csv
def main():
    f = open('q2.csv', 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')
    for i in range(7):
        i +=1
        header = next(data)

    max_diff= -999
    min_diff= 999
    max_date = ''
    min_date = ''

    for row in data:
        if row[-1] == '' or row[-2] == '' or row[-3] == '':
            continue
        else:
            row[-1] = float(row[-1])
            row[-2] = float(row[-2])

            diff = row[-1] - row[-2]

            if max_diff < diff:
                max_date = row[0]
                max_diff = diff
            if min_diff > diff:
                min_date = row[0]
                min_diff = diff
    
        
    f.close()

    print('*** Annual Temperature Report for Seoul in 2022 ***')
    print(f'Day with the Largest Temperature Variation: {max_date}')
    print(f'Maximum Temperature Difference: {round(max_diff, 2)} Celsius')
    print(f'Day with the Smallest Temperature Variation: {min_date}')
    print(f'Minimum Temperature Difference: {round(min_diff, 2)} Celsius')

if __name__ =="__main__":
    main()