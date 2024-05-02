class LevenshteinAutomaton:
    def __init__(self, string, n):
        self.string = string
        self.max_edits = n

  <extra_id_0> def <extra_id_1>  <extra_id_2>    return range(len(self.string)+1)

   <extra_id_3> step(self, state, c):
   <extra_id_4>    new_state = [state[0]+1]
        for i in range(len(state)-1):
            cost = 0 if <extra_id_5> c else 1
      <extra_id_6>     new_state.append(min(new_state[i]+1, state[i]+cost, state[i+1]+1))
        return [min(x,self.max_edits+1) for x in <extra_id_7>   def is_match(self, state):
  <extra_id_8> 