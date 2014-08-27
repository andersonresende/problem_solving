
def short_bubble_sort(items):
    """
    Function that sort a list of items, stop when not exchanges.
    It's more effective than normal bubble sort.
    """
    exchange = True
    rounds = len(items) - 1
    while exchange and rounds:
        exchange = False
        for index in range(0, rounds):
            if items[index] > items[index+1]:
                items[index], items[index+1] = items[index+1], items[index]
                exchange = True
        rounds -= 1
    return items


#create random integer list
import random
items = range(10)
random.shuffle(items)
print items
#call function
print short_bubble_sort(items)



