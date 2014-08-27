

T = input()
for i in range(T):
	N = input()
	h = 1
	for n in range(N):
		h = h * 2 if n % 2 == 0 else h + 1
	print h