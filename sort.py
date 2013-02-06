#Lexicographic sort to get the maximum/minimum number from an array of numbers.
from random import randint

def partition(list, start, end, pivotIndex, comparator=None):
	
	storeIndex = start
	pivotValue = list[pivotIndex]
	list[pivotIndex], list[end] = list[end], list[pivotIndex]

	for i in range(start, end - 1) :
		if comparator is None:
			if list[i] < pivotValue:
				list[i], list[storeIndex] = list[storeIndex], list[i]
				storeIndex += 1
		elif comparator(list[i], pivotValue):
			list[i], list[storeIndex] = list[storeIndex], list[i]
			storeIndex += 1
	
	list[end], list[storeIndex] = list[storeIndex], list[end]
	return storeIndex

			
def quickSortRange(list, start, end, comparator=None):
		
	if start < end:
		pivotIndex = partition(list, start, end, randint(start, end), comparator=comparator)
		quickSortRange(list, start, pivotIndex - 1, comparator=comparator)
		quickSortRange(list, pivotIndex + 1, end, comparator=comparator)

def quick_sort(list, comparator=None):	
	quickSortRange(list, 0, len(list) - 1, comparator=comparator)	
	

def lex_comparator(x, y):
	print x, y
	#print int(str(x)+str(y)), int(str(y)+str(x))
	#print int(str(x)+str(y)) <= int(str(y)+str(x))
	return int(str(x)+str(y)) < int(str(y)+str(x)) 
	
	#return cmp (int(str(x)+str(y)), int(str(y)+str(x)))	
	
