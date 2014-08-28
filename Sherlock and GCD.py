#https://www.hackerrank.com/challenges/sherlock-and-gcd
def getGCD(big, small) :
	a = big % small
	if a == 1 : 
		return 1
	elif a == 0:
		return small
	else:
		return getGCD(small, a)


T = input()
for i in range(0, T):
	N = input()
	num = [int(i) for i in raw_input().split(' ')]
	if 1 in num : 
		print 'YES'
		continue

	num.sort()
	find = False
	for index, small in enumerate(num):
		for big in num[index+1 :] :
			if getGCD(big, small) == 1 :
				print 'YES'
				find = True
				break
		if find:
			break
	if not find:
		print 'NO'


