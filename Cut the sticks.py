#https://www.hackerrank.com/challenges/cut-the-sticks


def cut(sticks):
	print len(sticks)
	if len(sticks) <= 1:
		return sticks, True

	sticks = map(lambda x: x - sticks[0], sticks)
	sticks = [i for i in sticks if i != 0]
	return sticks, False

N = input()
sticks = map(int, raw_input().strip().split())
sticks.sort()
while True:
	sticks, end = cut(sticks)
	if end or len(sticks) == 0:
		break