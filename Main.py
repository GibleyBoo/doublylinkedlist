#!/usr/bin/env
from dll import *

print('Press [ENTER] or type def for default list of integers to sort.')
print('DEFAULT LIST: [4, 3, 8, 10, 9, 6, 5, 7, 1, 2]')
print('Type def2 for a list of 100 random integers.')
print('Type a list in the form of: 1 2 3 4 5 6 7 8 9 10 for custom input.')
# LinkedList
ll = DoublyLinkedList
s = input('--> ')
if s == 'def' or s == '':
	arr = [4, 3, 8, 10, 9, 6, 5, 7, 1, 2]
elif s == 'def2':
	arr = []
	import random
	for i in range(1, 100):
		arr.append(random.choice(range(i)))
else:
	arr = list(map(int, s.split()))
print('array: ', arr)
print('objects to sort: ', len(arr))
print('press enter to start')
input('...')
print()

# Define lists -------- #######
bl = ll(arr)
ql = ll(arr)
ml = arr
hl = ll(arr)
sl = ll(arr)
il = ll(arr)
####### --------------- #######

# REMOVED--
"""
def fill(ll):
	for i in arr:
		ll.inject(i)
# fill lists
fill(bl)
fill(ql)
#fill(ml)
fill(sl)
fill(il)
"""
# --REMOVED

#print unsorted lists - #######
print('bl unsorted', bl)
print('ql unsorted', ql)
print('ml unsorted', ml)
#print('hl unsorted', hl)
print('sl unsorted', sl)
print('il unsorted', il)
####### --------------- #######

###
print()
###

#SORT ----------------- #######
# RECORDS TIME OF SORTINGS
import datetime
currtime = datetime.datetime.now
times = []

#BUBBLESORT ----------- #######
print('BUBBLESORT...')
begintime = currtime()
bl.bubblesort()
endtime = currtime()
print('DONE.')
times.append(endtime - begintime)
####### --------------- #######

#QUICKSORT ------------ #######
print('QUICKSORT...')
begintime = currtime()
ql.quicksort(1, len(ql))
endtime = currtime()
print('DONE.')
times.append(endtime - begintime)
####### --------------- #######
lists = []

# PART OF MERGESORT 
def merge_sort(A):
	if len(A) <= 1:
		return A
	lists.append(A)
	
	mid = int(len(A)/2)
	left = A[0:mid]
	right = A[mid:]
	lists.append(left)
	lists.append(right)

	left = merge_sort(left)
	right = merge_sort(right)

	return merge(left, right)

def merge(left, right):
	result = []

	while (len(left) > 0) and (len(right) > 0):
		if left[0] <= right[0]:
			result.append(left[0])
			left = left[1:]
		else:
			result.append(right[0])
			right = right[1:]

	while len(left) > 0:
		result.append(left[0])
		left = left[1:]
	while len(right) > 0:
		result.append(right[0])
		right = right[1:]
	return result

# USES PYTHON LIST INSTEAD OF CUSTOM 
#MERGESORT ------------ #######
print('MERGESORT...')
begintime = currtime()
ml = merge_sort(ml)
endtime = currtime()
print('DONE.')
times.append(endtime - begintime)
####### --------------- #######

# WIP
#HEAPSORT ------------- #######
""" 
print('HEAPSORT...')
begintime = currtime()
hl.heapsort()
endtime = currtime()
print('DONE.')
times.append(endtime - begintime)
"""
####### --------------- #######

#SELECTION SORT ------- #######
print('SELECTION SORT...')
begintime = currtime()
sl.sel()
endtime = currtime()
print('DONE.')
times.append(endtime - begintime)
####### --------------- #######

#INSERTION SORT ------- #######
print('INSERTION SORT...')
begintime = currtime()
il.ins()
endtime = currtime()
print('DONE.')
times.append(endtime - begintime)
####### --------------- #######

###
print()
###

# print sorted lists
print('bl sorted', bl)
print('ql sorted', ql)
print('ml sorted', ml)
#print('hl sorted', hl)
print('sl sorted', sl)
print('il sorted', il)
####### --------------- #######

###
print()
###

# print times --------- #######
for time in times:
	print(time)
####### --------------- #######

###
print()
###