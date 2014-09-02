#https://www.hackerrank.com/challenges/tutorial-intro


def quickSort(array):
	pivot = array[-1]
	blankpos = 0
	global quickcount
	for i in range(0, len(array)):
		if array[i] <= pivot:
			array[i], array[blankpos] = array[blankpos], array[i]
			blankpos = blankpos + 1
			
	blankpos = blankpos - 1
	if len(array[: blankpos]) > 1:
		array[: blankpos] = quickSort(array[: blankpos])
	if len(array[blankpos + 1:]) > 1:
		array[blankpos + 1:] = quickSort(array[blankpos + 1:])

	return array


V = input()
N = input()
li = map(int, raw_input().strip().split())

li = quickSort(li)
print li.index(V)