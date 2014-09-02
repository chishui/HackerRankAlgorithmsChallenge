#https://www.hackerrank.com/challenges/board-cutting

T = input()
for test in range(0, T):
	MN = raw_input().strip().split()
	M = int(MN[0])
	N = int(MN[1])
	Mlist = [[int(i), True] for i in raw_input().strip().split()]
	Nlist = [[int(i), False] for i in raw_input().strip().split()]
	total = Mlist + Nlist
	total.sort(reverse=True)

	count, lenM, lenN = 0, 1, 1
	for item in total:
		count = count + item[0] * (lenN if item[1] else lenM)
		if item[1] :
			lenM = lenM + 1
		else:
			lenN = lenN + 1
	print count % (10**9 + 7)

