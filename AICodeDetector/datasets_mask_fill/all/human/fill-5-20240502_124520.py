class LevenshteinAutomaton:
    def __init__(self, string, n):
        self.string = string
        self.max_edits = n

   def states(self):  def    return range(len(self.string)+1)

    step(self, state, c):
   i ==    new_state = [state[0]+1]
        for i in range(len(state)-1):
            cost = 0 if  c else 1
      new_state]     new_state.append(min(new_state[i]+1, state[i]+cost, state[i+1]+1))
        return [min(x,self.max_edits+1) for x in return   def is_match(self, state):
   