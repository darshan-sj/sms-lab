# ks

from random import random

N = 10
r = [random() for i in range(N)]
# N, r = 5, [0.44, 0.81, 0.14, 0.05, 0.93]
D_alpha = 0.565

r.sort()

D_plus_list = [(i/N) - r[i-1] for i in range(1, N+1)]
D_plus = max(D_plus_list)

D_minus_list = [r[i-1] - ((i-1)/N) for i in range(1, N+1)]
D_minus = max(D_minus_list)

# print(D_plus_list)
# print(D_minus_list)

D = max(D_plus, D_minus)

if D <= D_alpha:
	print('Failed to reject the uniformity hypothesis.')
else:
	print('Uniformity hypothesis rejected!')