#https://www.hackerrank.com/challenges/manasa-and-stones

T = input()
for i in range(0, T):
	n = input()
	a = input()
	b = input()

	s = []
	for index in range(0, n):
		value = index * b + (n - index - 1) * a
		if value not in s :
			s.append(value)
	s = sorted(s)
	print ' '.join([str(i) for i in s])

