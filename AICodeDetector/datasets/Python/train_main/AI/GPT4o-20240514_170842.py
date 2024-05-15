
    """
    Спуск из вершины curr по строке s с кэшированием
    """
    for char in s:
        if char in self.cache[curr]:
            curr = self.cache[curr][char]
        else:
            if char in self.edges[curr]:
                next_node = self.edges[curr][char]
                self.cache[curr][char] = next_node
                curr = next_node
            else:
                return None
    return curr
