import csv
import random

DAYS = 20
CP = 0.33
SP = 0.5
SP_scrap = 0.05
STOCK = 70

demand = [40, 50, 60, 70, 80, 90, 100]
good_prob = [0.03, 0.05, 0.15, 0.20, 0.35, 0.15, 0.07]
fair_prob = [0.1, 0.18, 0.4, 0.2, 0.08, 0.04, 0.0]
poor_prob = [0.44, 0.22, 0.16, 0.12, 0.06, 0.0, 0.0]
day_prob = [0.35, 0.45, 0.2]

day_random = [94, 77, 49, 45, 43, 32, 49, 0, 16, 24, 31, 14, 41, 61, 85, 8, 15, 97, 52, 78]
demand_random = [80, 20, 15, 88, 98, 65, 86, 73, 24, 60, 60, 29, 18, 90, 93, 73, 21, 45, 76, 96]

day_rd = [0] * 3
good_rd = [0] * 7
fair_rd = [0] * 7
poor_rd = [0] * 7

day_rd[0], good_rd[0], fair_rd[0], poor_rd[0] = int(day_prob[0] * 100), int(good_prob[0] * 100), int(fair_prob[0] * 100), int(poor_prob[0] * 100)
for i in range(1, 7):
	good_rd[i] = good_rd[i-1] + int(good_prob[i] * 100)
	fair_rd[i] = fair_rd[i-1] + int(fair_prob[i] * 100)
	poor_rd[i] = poor_rd[i-1] + int(poor_prob[i] * 100)
for i in range(1, 3):
	day_rd[i] = day_rd[i-1] + int(day_prob[i] * 100)

def table_lookup(r, x):
	t = 0
	if not x:
		# check newsday type
		# return 0 => good, 1 => fair and 2 => poor
		if r == 0:
			t = 2
		elif r <= day_rd[0]:
			t = 0
		else:
			for i in range(1, len(day_rd)):
				if r > day_rd[i-1] and r <= day_rd[i]:
					t = i
					break
	elif x == 1:
		if r == 0:
			t = demand[-1]
		elif r <= good_rd[0]:
			t = demand[0]
		else:
			for i in range(1, len(good_rd)):
				if r > good_rd[i-1] and r <= good_rd[i]:
					t = demand[i]
					break
	elif x == 2:
		if r == 0:
			t = demand[-1]
		elif r <= fair_rd[0]:
			t = demand[0]
		else:
			for i in range(1, len(fair_rd)):
				if r > fair_rd[i-1] and r <= fair_rd[i]:
					t = demand[i]
					break
	elif x == 3:
		if r == 0:
			t = demand[-1]
		if r <= poor_rd[0]:
			t = demand[0]
		else:
			for i in range(1, len(poor_rd)):
				if r > poor_rd[i-1] and r <= poor_rd[i]:
					t = demand[i]
					break
	return t


columns = ['Day', 'Newsday RN', 'Type of Newsday', 'Demand RN', 'Demand', 'Revenue', 'Lost Profit', 'Salvage', 'Daily Profit']
day = ['Good', 'Fair', 'Poor']

row = [0] * DAYS

for i in range(DAYS):
	row[i] = [0] * len(columns)
	row[i][0] = i + 1
	row[i][1] = day_random[i]
	day_type = table_lookup(day_random[i], 0)
	row[i][2] = day[day_type]
	row[i][3] = demand_random[i]
	row[i][4] = table_lookup(demand_random[i], day_type+1)
	if row[i][4] <= STOCK:
		row[i][5] = row[i][4] * SP
		row[i][6] = 0
		row[i][7] = (70 - row[i][4]) * SP_scrap
	else:
		row[i][5] = STOCK * SP
		row[i][6] = round((row[i][4] - 70) * (SP - CP), 1)
	row[i][8] = round(row[i][5] - row[i][6] + row[i][7] - STOCK * CP, 1)

with open('q3.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(columns)
	for i in row:
		writer.writerow(i)
