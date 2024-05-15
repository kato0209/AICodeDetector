
    if self.start_symbol == self.start_symbol_with_start_symbol:
      return self.start_symbol
    if self.start_symbol_with_end_symbol == self.end_symbol:
      return self.end_symbol
    if self.end_symbol == self.end_symbol_with_start_symbol:
      return self.start_symbol
    if self.end_symbol_with_start_symbol == self.start_symbol_with_end_symbol:
      return self.start_symbol
    if self.end_symbol_with_end_symbol ==