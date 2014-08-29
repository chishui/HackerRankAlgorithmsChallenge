#https://www.hackerrank.com/challenges/quicksort4

import copy
N = input()
num = [int(i) for i in raw_input().split(' ')]
num1 = copy.copy(num)
quickcount = 0
insertcount = 0
def quickSort(array):
	pivot = array[-1]
	blankpos = 0
	global quickcount
	for i in range(0, len(array)):
		if array[i] <= pivot:
			array[i], array[blankpos] = array[blankpos], array[i]
			blankpos = blankpos + 1
			quickcount = quickcount + 1
	blankpos = blankpos - 1
	if len(array[: blankpos]) > 1:
		array[: blankpos] = quickSort(array[: blankpos])
	if len(array[blankpos + 1:]) > 1:
		array[blankpos + 1:] = quickSort(array[blankpos + 1:])

	return array

def insertSort(array) : 
	global insertcount
	for i in range(0, len(array)):
		j = i - 1
		while j >= 0:
			if array[i] < array[j] :
				array[i] , array[j] = array[j] , array[i]
				insertcount = insertcount + 1
				i = i - 1
				j = j - 1
			else:
				break
			
	return array

quickSort(num)
insertSort(num1)
print insertcount - quickcount


