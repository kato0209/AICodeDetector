import tensorflow as tf


class DFA:

	def _normalize(self, productions):
		symbols = [] for production in tf.unstack(productions, axis=1): lhs, rhs = self.production_rules[tf.argmax(input=production, axis=-1)] if not symbols: # first iteration if lhs != self.start_symbol: raise ValueError("`productions` must begin with `self.start_symbol`.") if rhs: symbols = rhs else: # next iteration, if rhs not in symbols: raise ValueError("`productions` must end with `self.end_symbol`.")

		# create a mapping of lhs to nonterminal (or nil) symbols.
		lhs, _ finally and to build up the nonterminal symbols based on the first occurrence # in a linear sequence. index = symbols.index(lhs) symbols =