#https://www.hackerrank.com/challenges/sherlock-and-the-beast
T = input()
for i in range(0, T):	
	n = input()
	if n < 3 :
		print -1
		continue

	for i5 in range(0, n/3 + 1)[::-1]:
		if (n - i5 * 3) % 5 == 0:
			print '%s%s' %(i5 * 3 * '5', (n- i5 * 3) * '3')
			break
		if i5 == 0:
			print -1
