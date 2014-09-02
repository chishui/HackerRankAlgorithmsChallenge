#https://www.hackerrank.com/challenges/countingsort3

N = input()
li = [int(raw_input().strip().split()[0]) for i in range(0, N)]

li.sort()
last = -1
index = 0
out = []
for i in range(0, 100):
	while index < len(li) and i >= li[index] :
		index = index + 1
	out.append(index)

print ' '.join(map(str, out))



