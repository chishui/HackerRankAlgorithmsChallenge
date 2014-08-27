#https://www.hackerrank.com/challenges/service-lane
NandT = raw_input()
N = int(NandT.split(' ')[0])
T = int(NandT.split(' ')[1])
widthstr = raw_input()
width = widthstr.split(' ')

for t in range(T):
	test = raw_input()
	i = int(test.split(' ')[0])
	j = int(test.split(' ')[1])
	print min(width[i : j+1])