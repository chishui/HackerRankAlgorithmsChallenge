
def fibonacci() :
	a, b, c = 0, 0, 1
	while True:
		yield b
		a, b, c = b, c, b + c

#https://www.hackerrank.com/challenges/is-fibo
T = input()
nums = [[input(), i] for i in range(0, T)]
nums.sort()

fib = fibonacci()
lastfib = fib.next()
for num in nums:
	while True:
		if num[0] == lastfib :
			num.append('IsFibo')
			break
		elif num[0] < lastfib :
			num.append('IsNotFibo')
			break

		lastfib = fib.next()
nums = sorted(nums, key = lambda x:x[1])
for num in nums:
	print num[2]