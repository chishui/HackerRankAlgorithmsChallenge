#https://www.hackerrank.com/challenges/quicksort1
#!/bin/python


def partition(ar):    	
	pivot = ar[0]
	small = []
	big = []
	for i in range(1, len(ar)):
		if ar[i] < pivot :
			small.append(ar[i])
		elif ar[i] > pivot:
			big.append(ar[i])
	small.append(pivot)
	small = small + big

	return ' '.join(map(str, small))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
print partition(ar)
