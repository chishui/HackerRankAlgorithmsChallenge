#https://www.hackerrank.com/challenges/game-of-rotation

N = input()
li = map(int, raw_input().strip().split())
count = sum(li)
maxcount = sum([(i+1) * item for i, item in enumerate(li)])
PMEAN = maxcount
for i in range(1, len(li))[::-1]:
	PMEAN = PMEAN + count - len(li) * li[i]
	if maxcount < PMEAN:
		maxcount = PMEAN	

print maxcount