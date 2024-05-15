
    """
    Включает кэширование запросов к descend
    """
    original_descend = self.descend
    cache = {}

        if args in cache:
            return cache[args]
        result = original_descend(*args)
        cache[args] = result
        return result

    self.descend = cached_descend
