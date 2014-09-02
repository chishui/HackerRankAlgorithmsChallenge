#https://www.hackerrank.com/challenges/make-it-anagram
A = map(ord, list(raw_input().strip()))
B = map(ord, list(raw_input().strip()))
A.sort()
B.sort()

count, i, j = 0, 0, 0
while i < len(A) and j < len(B) :
	if A[i] < B[j] :
		count = count + 1
		i = i + 1
	elif A[i] > B[j]:
		count = count + 1
		j = j + 1
	else :
		i = i + 1
		j = j + 1

if i == len(A) :
	count = count + len(B) - j
if j == len(B):
	count = count + len(A) - i
print count