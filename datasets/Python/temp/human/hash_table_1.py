import hashlib


class LinkedList():

    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class HashTable():

    def __init__(self, length):
        self.table = [None for _ in range(length)]
        self.length = length

    def _hash(self, key):
        key = str(key)
        hash = hashlib.md5(key.encode()).hexdigest()
        return int(hash, 16) % self.length

    def add(self, key, value):
        index = self._hash(key)
        node = self.table[index]
        while True:
            if node is None:
                self.table[index] = LinkedList(key, value)
                break
            if node.key == key:
                node.value = value
                break
            if node.next is None:
                node.next = LinkedList(key, value)
                break
            node = node.next

    def get(self, key):
        index = self._hash(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def remove(self, key):
        index = self._hash(key)
        node = self.table[index]
        previous = None
        while node:
            if node.key == key:
                if previous is None and node.next is None:
                    self.table[index] = None
                    break
                elif previous and node.next:
                    previous.next = node.next
                    break
                elif node.next:
                    self.table[index] = node.next
                    break
                elif previous:
                    previous.next = None
                    break
            else:
                previous = node
                node = node.next

    def print_all_items(self):
        for i in range(self.length):
            print('----------------------------')
            print(f'Index is {i}')
            node = self.table[i]
            while node:
                print(f'{node.key}: {node.value}')
                node = node.next
            print('----------------------------')