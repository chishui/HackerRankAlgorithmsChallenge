#https://www.hackerrank.com/challenges/Two-arrays
T = input()
for t in range(0, T):
	NK = raw_input().split(' ')
	N = int(NK[0])
	K = int(NK[1])
	A = [int(i) for i in raw_input().split(' ')]
	B = [int(i) for i in raw_input().split(' ')]
	A.sort()
	B.sort()
	res = 'YES'
	for i in range(0, N):
		if A[i] + B[-(i + 1)] < K:
			res = 'NO'
			break
	print res