import csv
def main():
    f = open('q1.csv', 'r', encoding="cp949")
    data = csv.reader(f, delimiter=',')
    for i in range(7):
        i +=1
        header = next(data)

    full_date = 0.0
    sum_avg_temp = 0.0
    sum_min_temp = 0.0
    sum_max_temp = 0.0

    avg_avg_temp= 0.0
    avg_min_temp= 0.0
    avg_max_temp= 0.0

    for row in data:
        if row[-1] == '' or row[-2] == '' or row[-3] == '':
            continue
        else:
            row[-1] = float(row[-1])
            row[-2] = float(row[-2])
            row[-3] = float(row[-3])
            full_date += 1
            sum_avg_temp += row[-3]
            sum_min_temp += row[-2]
            sum_max_temp += row[-1]

    avg_avg_temp = sum_avg_temp / full_date
    avg_min_temp = sum_min_temp / full_date
    avg_max_temp = sum_max_temp / full_date

    f.close()

    print('*** Annual Temperature Report for Seoul in 2022 ***')
    print(f'Average Temperature {round(avg_avg_temp, 2)} Celsius')
    print(f'Average Minimum Temperature: {round(avg_min_temp, 2)} Celsius')
    print(f'Average Maximum Temperature: {round(avg_max_temp, 2)} Celsius')

if __name__ =="__main__":
    main()