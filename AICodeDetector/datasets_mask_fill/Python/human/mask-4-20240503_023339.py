class LevenshteinAutomaton:
    def __init__(self, string, n):
        self.string = string
        self.max_edits = n

    def start(self):
        return range(len(self.string)+1)

    def step(self, state, c):
  <extra_id_0>   <extra_id_1> new_state = [state[0]+1]
 <extra_id_2>      for i <extra_id_3>  <extra_id_4>         cost = 0 if self.string[i] == c <extra_id_5>    <extra_id_6>       new_state.append(min(new_state[i]+1, state[i]+cost, state[i+1]+1))
        return [min(x,self.max_edits+1) for <extra_id_7> new_state]

    def is_match(self, state):
 <extra_id_8>  