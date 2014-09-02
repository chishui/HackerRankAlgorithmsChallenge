#https://www.hackerrank.com/challenges/sherlock-and-array

T = input()
for test in range(0, T):
	N = input()
	li = map(int, raw_input().split())
	if len(li) == 2:
		print "NO"
		continue
	if len(li) == 1:
		print "YES"
		continue
	find = False
	sumleft = None
	sumright = None
	for i in range(1, len(li) - 1): 
		sumleft = sumleft + li[i-1] if sumleft else sum(li[:1])
		sumright = sumright - li[i] if sumright else sum(li[2:])
		if sumleft == sumright :
			find = True
			break

	print "YES" if find else "NO"