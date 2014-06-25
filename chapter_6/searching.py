# def sequentialSearch(alist, item):
#     pos = 0
#     found = False

#     while pos < len(alist) and not found:
#         if alist[pos] == item:
#             found = True
#         else:
#             pos = pos+1

#     return found

# testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(sequentialSearch(testlist, 3))
# print(sequentialSearch(testlist, 13))


# def orderedSequentialSearch(alist, item):
#     pos = 0
#     found = False
#     stop = False
#     while pos < len(alist) and not found and not stop:
#         if alist[pos] == item:
#             found = True
#         else:
#             if alist[pos] > item:
#                 stop = True
#             else:
#                 pos = pos+1

#     return found

# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# print(orderedSequentialSearch(testlist, 3))
# print(orderedSequentialSearch(testlist, 13))


# def binarySearch(alist, item):
#     first = 0
#     last = len(alist)-1
#     found = False

#     while first<=last and not found:
#         midpoint = (first + last)//2
#         if alist[midpoint] == item:
#             found = True
#         else:
#             if item < alist[midpoint]:
#                 last = midpoint-1
#             else:
#                 first = midpoint+1

#     return found
  
# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# print(binarySearch(testlist, 3))
# print(binarySearch(testlist, 13))




def recursive_sequential_search(lista, a):
    if not lista:
        return False
    if a == lista[0]:
        return True
    return recursive_sequential_search(lista[1:], a)

print recursive_sequential_search([1,2,3], 4)
