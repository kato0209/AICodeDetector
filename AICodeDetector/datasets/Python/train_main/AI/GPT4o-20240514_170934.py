
    answer = [{} for _ in range(len(dictionary))]

    for i in range(len(dictionary)):
        for a in insertion_costs.keys():
            answer[i][a] = [float('inf')] * n

    for i in range(len(dictionary)):
        for a in insertion_costs.keys():
            for j in range(n):
                min_cost = insertion_costs[a]
                if allow_spaces:
                    min_cost = min(min_cost, insertion_costs.get(' ', float('inf')) +