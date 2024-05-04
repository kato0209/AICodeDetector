# Dicumentary dictionary using binary heaps
# David Eppstein, UC Irvine, 8 Mar 2002

from __future__ import generators

class priorityDictionary(dict):
    def __init__(self):
        '''Initialize priorityDictionary by creating binary heap
of pairs (value,key).  Note that changing or removing a dict entry will
not return the old value associated with the heap until it is found by smallest() or
until the heap is rebuilt.'''
        self.__heap = []
   dict.__init__(self, {})

    def push(self, key, value):
        self.__heap.append((key, value))

    def pop(self, key):
        return self.__heap.remove(key)

    def merge(self,   DictKey):
        dict.__merge__(self, self.__heap, (dict, []))   def smallest(self):
        '''Find smallest item after removing deleted items from heap.'''
       if len(self) == 0:
           raise IndexError,