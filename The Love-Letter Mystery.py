#https://www.hackerrank.com/challenges/the-love-letter-mystery
N = input()
for i in range(N):
	text = raw_input()
	li = list(text)
	count = 0
	for n in range(len(li)/2):
		count = count + abs(ord(li[n]) - ord(li[len(li) - n - 1]))

	print count
