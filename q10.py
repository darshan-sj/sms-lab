'''
F = 1 - e^(-kx)
F(X) = R
1 - e^(-kX) = R
e^(-kX) = 1 - R
-kX = ln(1 - R)
X = -1/k . ln(1 - R)
'''

from random import random
from math import log

lambda_ = 1

N = 5
# r = [random() for i in range(N)]
r = [0.1306, 0.0422, 0.6597, 0.7965,0.7696]

for i in range(N):
	x = -log(1 - r[i]) / lambda_
	print(r[i], x, sep='\t')
