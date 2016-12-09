import csv
import random

T = 60

arrival = [i for i in range(1, 5)]
arrival_prob = [0.25, 0.4, 0.2, 0.15]

abel_service = [i for i in range(2, 6)]
abel_service_prob = [0.30, 0.28, 0.25, 0.17]

baker_service = [i for i in range(3, 7)]
baker_service_prob = [0.35, 0.25, 0.2, 0.2]

arrival_random = [26, 98, 90, 29, 42, 74, 80, 68, 22, 48, 34, 45, 24, 34, 63, 38, 80, 42, 56, 89, 18, 51, 71, 16, 92]
service_random = [95, 21, 51, 92, 89, 38, 13, 61, 50, 49, 39, 53, 88, 1, 81, 53, 81, 64, 1, 67, 1, 47, 75, 57, 87, 47]

abel_rd = [0] * 4
baker_rd = [0] * 4
arrival_rd = [0] * 4

# calculate random digits for the cumulative probability
abel_rd[0], baker_rd[0], arrival_rd[0] = int(abel_service_prob[0] * 100), int(baker_service_prob[0] * 100),int(arrival_prob[0] * 1000)
for i in range(4):
	abel_rd[i] = abel_rd[i-1] + int(abel_service_prob[i] * 100)
	baker_rd[i] = baker_rd[i-1] + int(baker_service_prob[i] * 100)
	arrival_rd[i] = arrival_rd[i-1] + int(arrival_prob[i] * 100)

def table_lookup(r, x):
	# x = 0 => arrival, x = 1 => abel, x = 2 => baker
	t = 0
	if not x:
		# arrival
		if r == 0:
			t = arrival[-1]
		elif r < arrival_rd[0]:
			t = arrival[0]
		else:
			for i in range(1, len(arrival_rd)):
				if r > arrival_rd[i-1] and r <= arrival_rd[i]:
					t = arrival[i]
					break
	elif x == 1:
		# abel
		if r == 0:
			t = abel_service[-1]
		wlif r <= abel_rd[0]:
			t = abel_service[0]
		else:
			for i in range(1, len(abel_rd)):
				if r > abel_rd[i-1] and r <= abel_rd[i]:
					t = abel_service[i]
					break
	else:
		# baker
		if r == 0:
			t = baker_service[-1]
		elif r <= baker_rd[0]:
			t = baker_service[0]
		else:
			for i in range(1, len(baker_rd)):
				if r > baker_rd[i-1] and r <= baker_rd[i]:
					t = baker_service[i]
					break
	return t

columns = ['Customer', 'Interarrival Time', 'Clock', 'Abel Service Begin', 'Abel Service Time', 'Abel Service End', 'Baker Service Begin', 'Baker Service Time', 'Baker Service End', 'Time in Queue', 'Time in System']

abel_free = True
row = []
row.append([])
arrival_time = 0
abel_time = table_lookup(service_random[0], 1)
row[0] = [1, arrival_time, 0, 0, abel_time, abel_time, 0, '-', '-', '-', abel_time]
abel_last = 0
baker_last = -1

i = 0
# fix this condition
while i < len(service_random)-1:
	i += 1
	row.append([])
	arrival_time = table_lookup(arrival_random[i-1], 0)
	row[i] = [0] * len(columns)
	row[i][0] = i + 1
	row[i][1] = arrival_time
	row[i][2] = row[i-1][2] + arrival_time
	
	if row[i][2] < row[abel_last][5] and row[baker_last][8] < row[abel_last][5]:
		abel_free = False
	else:
		abel_free = True

	if abel_free:
		service_time = table_lookup(service_random[i], 1)
		row[i][3] = max(row[abel_last][5], row[i][2])
		abel_last = i
		row[i][4] = service_time
		row[i][5] = row[i][3] + row[i][4]
		for col in range(6, 9):
			row[i][col] = '-'
		row[i][9] = row[i][3] - row[i][2]
		row[i][10] = row[i][5] - row[i][2]
	else:
		service_time = table_lookup(service_random[i], 2)
		for col in range(3, 6):
			row[i][col] = '-'
		if baker_last != -1:
			row[i][6] = max(row[baker_last][8], row[i][2])
		else:
			row[i][6] = row[i][2]
		baker_last = i
		row[i][7] = service_time
		row[i][8] = row[i][6] + row[i][7]
		row[i][9] = row[i][6] - row[i][2]
		row[i][10] = row[i][8] - row[i][2]

with open('q2.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(columns)
	for i in row:
		writer.writerow(i)
	