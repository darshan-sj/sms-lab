import csv
from random import random

N = 100
r = [random() for i in range(100)]

# 10 intervals
intervals = [0] * 10
for i in range(N):
	if r[i] < 0.1:
		intervals[0] += 1
	elif r[i] < 0.2:
		intervals[1] += 1
	elif r[i] < 0.3:
		intervals[2] += 1
	elif r[i] < 0.4:
		intervals[3] += 1
	elif r[i] < 0.5:
		intervals[4] += 1
	elif r[i] < 0.6:
		intervals[5] += 1
	elif r[i] < 0.7:
		intervals[6] += 1
	elif r[i] < 0.8:
		intervals[7] += 1
	elif r[i] < 0.9:
		intervals[8] += 1
	else:
		intervals[9] += 1

columns = ['Interval', 'Oi', 'Ei', 'Oi - Ei', '(Oi - Ei)^2', '((Oi - Ei)^2)/Ei']

E = N // len(intervals)
row = []
for i in range(len(intervals)):
	row.append([])
	row[i] = [0] * len(columns)
	row[i][0] = i + 1
	row[i][1] = intervals[i]
	row[i][2] = E
	row[i][3] = row[i][1] - E
	row[i][4] = row[i][3] ** 2
	row[i][5] = row[i][4] / E

x = sum(col[-1] for col in row)
x_alpha_d = 16.9	# d = n - 1, where n = no. of intervals
print('x = ', x, 'x_alpha_d =', x_alpha_d)
if x <= x_alpha_d:
	print('Failed to reject the uniformity hypothesis.')
else:
	print('Uniformity hypothesis rejected!')

with open('q7.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(columns)
	for i in row:
		writer.writerow(i)
	