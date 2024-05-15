
        if self.euristics is None:
            return
        # вычисление минимальной стоимости операции,
        # приводящей к появлению ('+') или исчезновению ('-') данного символа
        removal_costs = {a : np.inf for a in self.alphabet}
        insertion_costs = {a : np.inf for a in self.alphabet}
        if self.allow_spaces:
            removal_costs[' '] = np.inf
            insertion_costs[' '] = np.inf
    