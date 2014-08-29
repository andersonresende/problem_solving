def bubble_sort(lst):
    """Bubble sort standard, loop many times for each item, it's not good"""
    qt = len(lst)
    for q in range(qt, 0,  -1):
        for i in range(0,q-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst

#call function
print "Bubble sort"
print bubble_sort([7, 5, 8, 3, 4, 2, 9])


def short_bubble_sort(lst):
    """
    Function that sort a list, stop when not exchanges.
    It's more effective than normal bubble sort.
    """
    exchange = True
    rounds = len(lst) - 1
    while exchange and rounds:
        exchange = False
        for index in range(0, rounds):
            if lst[index] > lst[index+1]:
                lst[index], lst[index+1] = lst[index+1], lst[index]
                exchange = True
        rounds -= 1
    return lst


#create random list
import random
lst = range(10)
random.shuffle(lst)
#call function
print "Short bubble sort:"
print "Unordered lst: %s" % lst
print "Ordered lst: %s" % short_bubble_sort(lst)


