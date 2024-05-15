
    """
    Обратная топологическая сортировка
    """
        visited.add(node)
        for neighbor in trie[node]:
            if neighbor not in visited:
                dfs(neighbor, visited, stack)
        stack.append(node)

    visited = set()
    stack = []

    for node in trie:
        if node not in visited:
            dfs(node, visited, stack)

    return stack[::-1]
