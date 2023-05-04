import csv
f = open('q3.csv', 'r', encoding='cp949')
data = csv.reader(f)
header = next(data)

lines = ["1호선", "2호선", "3호선", "4호선", "5호선", "6호선", "7호선", "8호선", "9호선"]
lines_data = {"1호선":0, "2호선":0, "3호선":0, "4호선":0, "5호선":0, "6호선":0, "7호선":0, "8호선":0, "9호선":0}
max_line1 = 0
max_line2 = 0
min_line1 = 0
min_line1 = 0

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
        lines_data[row[1]] += row[4]+row[5]

s_line_data = sorted(lines_data.items(), key=lambda x:x[1], reverse=True)
print(s_line_data)

print('*** Subway Report for Seoul on March 2023 ***')
a = s_line_data[0][0].replace('호선', '')
print(f'1st Busiest Line: Line{a}, {s_line_data[0][1]}')
a = s_line_data[1][0].replace('호선', '')
print(f'2nd Busiest Line: Line{a}, {s_line_data[1][1]}')
a = s_line_data[-1][0].replace('호선', '')
print(f'1st Least used Line: Line{a}, {s_line_data[-1][1]}')
a = s_line_data[-2][0].replace('호선', '')
print(f'2nd Least used Line: Line{a}, {s_line_data[-2][1]}')

f.close()
