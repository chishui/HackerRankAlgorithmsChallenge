#https://www.hackerrank.com/challenges/sherlock-and-queries
NM = raw_input().split(' ')
N = int(NM[0])
M = int(NM[1])
A = [int(i) for i in raw_input().split(' ')]
B = [int(i) for i in raw_input().split(' ')]
C = [int(i) for i in raw_input().split(' ')]

maxnum = 10 ** 9 + 7

countdict = {}
for index, item in enumerate(B):
	countdict[item] = countdict.get(item, 1) * C[index]


for b, count in countdict.items():
	power = count % maxnum
	j = 1
	k = j * b
	while k <= N:
		A[k-1] = A[k-1] * power
		j = j + 1
		k = j * b



maxnum = 10 ** 9 + 7
print ' '.join([str(i % maxnum) for i in A])