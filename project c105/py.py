import csv
import math
with open('data.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]
def f(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean=total/n
    return mean
squaredlist = []
for number in data:
    b = int(number)-f(data)
    b = b**2
    squaredlist.append(b)
sum = 0
for i in squaredlist:
    sum = sum + i
standarddeviation = sum/len(data)-1
deviation = math.sqrt(standarddeviation)
print(deviation)