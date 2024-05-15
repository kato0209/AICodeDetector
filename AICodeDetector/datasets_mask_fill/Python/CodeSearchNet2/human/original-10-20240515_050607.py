
        curr_agenda = [(self.root, [], 0)]
        for i, a in enumerate(s):
            next_agenda = []
            for curr, borders, cost in curr_agenda:
                if cost >= max_count:
                    continue
                child = self.graph[curr][self.alphabet_codes[a]]
               