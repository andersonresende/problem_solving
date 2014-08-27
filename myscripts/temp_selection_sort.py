#Por que nao setamos qualquer valor da lista como o maior em uma selection sort?
#Qual a diferenca entre a selection sort e a bubble sort? bubble faz mais trocas, no entanto, as
# duas percorrem os mesmos loops. Buble comprar item com o proximo item, select compara item com o maior que ja passou.


def selection_sort(lst):
    for loop in range(len(lst)-1, 0, -1):
        max_location = 0
        for l in range(1, loop+1):
            if lst[l] > lst[max_location]:
                max_location = l

        lst[loop], lst[max_location] = lst[max_location], lst[loop]
    return lst


print selection_sort([1, 2, 5, 3, 7, 4])


def while_selection_sort(lst):
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


for i in range(1, 6):
    print i

c = 1
while c < 6:
    print c
    c += 1












