# -*- coding: utf-8 -*-
from linked_list import UnorderedList

class GenUnorderedList(UnorderedList):
    """It's a UnordereList whith a generetor to loop over."""

    def __iter__(self):
        """Generetor thats loop a list"""
        current = self.head
        while current:
            yield current.getData()
            current = current.next


if __name__ == '__main__':
    lst = GenUnorderedList()
    for x in range(1,4):
        lst.add(x)

    print lst.__iter__()

    for l in lst:
        print l