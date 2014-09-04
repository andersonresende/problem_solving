# -*- conding:utf-8 -*-

def insertion_sort(lst):
	""" Function insertion sort compare actual number whith previus numbers"""
	for i in range(1, len(lst)):
		while i and lst[i] < lst[i-1]:
			lst[i], lst[i-1] = lst[i-1], lst[i]
			i-=1
	return lst

print insertion_sort([1,3,4,5,2,7,6])

def w_insertion_sort(lst):
	""" Function insertion sort on while loops"""
	cont = 1
	while cont < len(lst):
		i = cont
		while i and lst[i] < lst[i-1]:
			lst[i], lst[i-1] = lst[i-1], lst[i]
			i-=1
		cont+=1
	return lst

print insertion_sort([1,3,4,5,2,7,6])

