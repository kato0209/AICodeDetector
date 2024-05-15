from collections import deque 
import copy
import numpy as np
import random

answer = deque()
n, dictionary = 10, 2
removal_costs = [dict() for node in dictionary.data] if n == 0: return answer curr_alphabet = copy.copy(dictionary.alphabet) if allow_spaces: curr_alphabet += [' '] for l, (costs_in_node, node) in enumerate(zip(answer, dictionary.data)): # 1, symbol стоимости удаления символов curr_node_removal_costs = np.empty(dtype=np.float64, shape=(n,)) if len(node[0]) > 0: curr_node_removal_costs[0] = min(removal_costs[symbol] for answer in node[0]) for j, symbols in enumerate(node[1:],