#https://www.hackerrank.com/challenges/find-digits
T = input()
for i in range(0, T):
	N = input()
	out = [n for n in list(str(N)) if int(n) and int(N) % int(n) == 0]
	print len(out)
