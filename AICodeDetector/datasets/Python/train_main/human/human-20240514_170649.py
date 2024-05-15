
    symbols = []
    for production in tf.unstack(productions, axis=1):
      lhs, rhs = self.production_rules[tf.argmax(input=production, axis=-1)]
      if not symbols:  # first iteration
        if lhs != self.start_symbol:
          raise ValueError("`productions` must begin with `self.start_symbol`.")
        symbols = rhs
      else:
        # Greedily unroll the nonterminal symbols based on the first occurrence
        # in a linear sequence.
        index = symbols.index(lhs)
        symbols =