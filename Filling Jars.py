
NM = raw_input().split(' ')
N = int(NM[0])
M = int(NM[1])
count = 0
for i in range(0, M):
	candy = raw_input().split(' ')
	fro = int(candy[0])
	to = int(candy[1])
	num = int(candy[2])
	count = count + num * (to - fro + 1)

print count / N