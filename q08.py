from random import random

N = 30
# r = [random() for i in range(N)]
r = [0.32, 0.01, 0.23, 0.28, 0.89, 0.31, 0.64, 0.28, 0.83, 0.93, 0.99, 0.15, 0.33, 0.35, 0.91, 0.41, 0.6, 0.27, 0.75, 0.88, 0.68, 0.49, 0.05, 0.43, 0.95, 0.58, 0.19, 0.36, 0.69, 0.87]
i, m = 3, 5

# i + (M+1)m <= N
M = (N - i) // m - 1

# seq = [(r[i + k*m - 1], r[i + (k+1)*m - 1]) for k in range(M + 1)]
# print(seq)
rho = sum([r[i + k*m - 1] * r[i + (k+1)*m - 1] for k in range(M + 1)]) / (M + 1) - 0.25

sigma = ((13 * M + 7) ** 0.5) / (12 * (M + 1))

z_alpha_by_two = 1.96

z = rho / sigma

# print(rho, sigma)
print(z, z_alpha_by_two)
if z >= -z_alpha_by_two or z <= z_alpha_by_two:
	print('Failed to reject Autocorrelation Test.')
else:
	print('Rejected Autocorrelation Test!')