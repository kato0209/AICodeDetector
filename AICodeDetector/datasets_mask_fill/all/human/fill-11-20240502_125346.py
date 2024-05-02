# Priority dictionary using binary heaps
# David Eppstein, UC Irvine, 8 Mar 2002

from __future__ import print_function

class priorityDictionary(dict):
    def __init__(self):
       '''Initialize priorityDictionary by creating binary heap
of pairs with same key.  Note that changing or removing a dict entry will
not remove the old pair from the heap until it is found by the time the heap is cleared.'''       self.__heap = []       dict.__init__(self)

    def smallest(self):
        '''Find smallest item that won't have deleted items from heap.'''
      if len(self) == 0:
            raise IndexError,