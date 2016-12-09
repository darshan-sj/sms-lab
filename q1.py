import csv
import random

N = 20

service = [i for i in range(1, 7)]
service_prob = [0.1, 0.2, 0.3, 0.25, 0.1, 0.05]

arrival = [i for i in range(1, 9)]
arrival_prob = [0.125] * 8

service_random = [84, 10, 74, 53, 17, 79, 91, 67, 89, 38, 32, 94, 79, 5, 79, 84, 52, 55, 30, 50]
arrival_random = [913, 727, 15, 948, 309, 922, 753, 235, 302, 109, 93, 607, 738, 359, 888, 106, 212, 493, 535]

service_rd = [0] * 6
arrival_rd = [0] * 8

# calculate random digits for the cumulative probability
service_rd[0], arrival_rd[0] = int(service_prob[0] * 100), int(arrival_prob[0] * 1000)
for i in range(6):
	service_rd[i] = service_rd[i-1] + int(service_prob[i] * 100)
for i in range(8):
	arrival_rd[i] = arrival_rd[i-1] + int(arrival_prob[i] * 1000)

columns = ['Customer', 'Interarrival Time', 'Clock', 'Service Begin', 'Service Time', 'Service End', 'Time in Queue', 'Time in System']

def table_lookup(r, x):
	# x = 0 => arrival, x = 1 => service
	t = 0
	if x:
		# service
		if r == 0:
			t = service[-1]
		elif r <= service_rd[0]:
			t = service[0]
		else:
			for i in range(1, len(service_rd)):
				if r > service_rd[i-1] and r <= service_rd[i]:
					t = service[i]
					break
	else:
		# arrival
		if r == 0:
			t = service[-1]
		elif r < arrival_rd[0]:
			t = arrival[0]
		else:
			for i in range(1, len(arrival_rd)):
				if r > arrival_rd[i-1] and r <= arrival_rd[i]:
					t = arrival[i]
					break
	return t

row = [0] * N
arrival_time = 0
service_time = table_lookup(service_random[0], 1)
row[0] = [1, arrival_time, 0, 0, service_time, service_time, 0, service_time]
for i in range(1, N):
	arrival_time = table_lookup(arrival_random[i-1], 0)
	service_time = table_lookup(service_random[i], 1)
	row[i] = [0] * len(columns)
	row[i][0] = i + 1
	row[i][1] = arrival_time
	row[i][2] = row[i-1][2] + arrival_time
	row[i][3] = max(row[i-1][5], row[i][2])
	row[i][4] = service_time
	row[i][5] = row[i][3] + row[i][4]
	row[i][6] = row[i][3] - row[i][2]
	row[i][7] = row[i][5] - row[i][2]

with open('q1.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(columns)
	for i in row:
		writer.writerow(i)
