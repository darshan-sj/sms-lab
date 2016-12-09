'''
1. n = 0, p = 1
2. generate r, p = p * r
3. if p < e^-alpha, accept
'''

from random import random
from math import exp

N = 3
alpha = 0.2

# r = [random() for i in range(5)]
rand = [0.4357, 0.4146, 0.8353, 0.9187, 0.8001]

variates = []


i = 0
n, p = 0, 1
while True:
	if len(variates) >= N:
		break
	r = rand[i]
	p = p * r
	if p < exp(-alpha):
		variates.append(n)
		n, p = 0, 1
	else:
		n += 1
	i += 1

print(variates)
