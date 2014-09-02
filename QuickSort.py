#https://www.hackerrank.com/challenges/quicksort2

def quickSort(ar):    
	pivot = ar[0]
	small = []
	big = []
	for i in range(1, len(ar)):
		if ar[i] < pivot :
			small.append(ar[i])
		elif ar[i] > pivot:
			big.append(ar[i])
	if len(small) >= 2:
		small = quickSort(small)
	if len(big) >= 2:
		big = quickSort(big)

	small.append(pivot) 
	small = small + big
	print ' '.join(map(str, small))
	return small

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)