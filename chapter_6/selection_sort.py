def selection_sort(lst):
    """
    Function select sort that order a list.
    """
    for loop in range(len(lst)-1, 0, -1):
        max_location = 0
        for l in range(1, loop+1):
            if lst[l] > lst[max_location]:
                max_location = l

        lst[loop], lst[max_location] = lst[max_location], lst[loop]
    return lst


print selection_sort([1, 2, 5, 3, 7, 4])


def while_selection_sort(lst):
    """
    Function select sort that order a list,
    Implements whith while loops instead for.
    """
    cont = len(lst) - 1
    while cont:
        c = 1
        max_location = 0
        while c < cont+1:
            if lst[c] > lst[max_location]:
                max_location = c
            c += 1
        lst[cont], lst[max_location] = lst[max_location], lst[cont]
        cont -= 1
    return lst


print while_selection_sort([1, 2, 5, 3, 7, 4])












