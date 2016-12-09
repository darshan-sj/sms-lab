import csv
import random

M, N = 11, 5
CYCLE = 5

demand = [i for i in range(5)]
demand_prob = [0.1, 0.25, 0.35, 0.21, 0.09]
lead = [i for i in range(1, 4)]
lead_prob = [0.6, 0.3, 0.1]


demand_rd = [0] * len(demand_prob)
lead_rd = [0] * len(lead_prob)

demand_rd[0], lead_rd[0] = int(demand_prob[0] * 100), int(lead_prob[0] * 10)
for i in range(1, len(demand_prob)):
	demand_rd[i] = demand_rd[i-1] + int(demand_prob[i] * 100)
for i in range(1, len(lead_prob)):
	lead_rd[i] = lead_rd[i-1] + int(lead_prob[0] * 10)

demand_random = [24, 35, 65, 81, 54, 3, 87, 27, 73, 70, 47, 45, 48, 17, 9, 42, 87, 26, 36, 40, 7, 63, 19, 88, 94]
lead_random = [5, 0, 3, 4, 8]

def table_lookup(r, x):
	# 0 => demand, 1 => lead
	t = 0
	if not x:
		# demand
		if r == 0:
			t = demand[-1]
		elif r < demand_rd[0]:
			t = demand[0]
		else:
			for i in range(1, len(demand_rd)):
				if r > demand_rd[i-1] and r <= demand_rd[i]:
					t = demand[i]
					break
	else:
		# lead
		if r == 0:
			t = lead[-1]
		elif r < lead_rd[0]:
			t = lead[0]
		else:
			for i in range(1, len(lead_rd)):
				if r > lead_rd[i-1] and r <= lead_rd[i]:
					t = lead[i]
					break
	return t

columns = ['Cycle', 'Day', 'Begin Inventory', 'Demand', 'End Inventory', 'Shortage', 'Order Quantity', 'Days until Order arrives']

row = [0] * (N * CYCLE)

cycle = 1
inventory = 3
days_until_arrival = 2
days_until_arrival -= 1
order_qty = 8
shortage = 0

total = N * CYCLE
for i in range(total):
	row.append([])
	row[i] = [0] * len(columns)
	row[i][0] = ''
	row[i][1] = i % 5 + 1
	if row[i][1] == 1:
		row[i][0] = cycle
	elif row[i][1] == 5:
		cycle += 1
	if days_until_arrival == -1:
		inventory += order_qty - shortage
		shortage = 0
	row[i][2] = inventory
	row[i][3] = table_lookup(demand_random[i], 0)
	remaining = row[i][2] - row[i][3]
	inventory = max(0, remaining)
	if remaining < 0:
		shortage = shortage - remaining
	row[i][4] = inventory
	row[i][5] = shortage
	if row[i][1] == 5:
		order_qty = M - row[i][4]
		row[i][6] = order_qty
		days_until_arrival = table_lookup(lead_random[cycle-2], 1)
		row[i][7] = days_until_arrival
	else:
		row[i][6] = '-'
	if days_until_arrival >= 0:
		row[i][7] = days_until_arrival
	days_until_arrival -= 1


with open('q4.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(columns)
	for i in row:
		writer.writerow(i)
