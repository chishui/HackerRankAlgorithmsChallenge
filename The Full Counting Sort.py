#https://www.hackerrank.com/challenges/countingsort4

N = input()

countmap = {}
for i in range(0, N):
	line = raw_input().strip().split()
	num = int(line[0])
	countmap.setdefault(num, [])
	if i < N/2 :
		countmap[num].append('-') 
	else :
		countmap[num].append(line[1]) 

out = []
for key, value in countmap.items():
	out.append(' '.join(value))
print ' '.join(out)

