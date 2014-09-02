#https://www.hackerrank.com/challenges/sherlock-and-squares
from math import sqrt, floor, ceil
T = input()
for test in range(0, T):
	AB = raw_input().strip().split()
	A = int(AB[0])
	B = int(AB[1])
	left = int(ceil(sqrt(A)))
	right = int(floor(sqrt(B)))
	count = 0
	if left <= right:
		print right - left + 1
	else :
		print 0

