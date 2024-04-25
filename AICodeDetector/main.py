from tokenize import tokenizer
from masking import tokenize_and_mask


example_code = """

import numpy as np
print("Hello, world!")

"""

tokens = tokenizer(example_code)
span_length = 2
pct = 0.3
buffer_size = 1
text = tokenize_and_mask(tokens, buffer_size, span_length, pct, ceil_pct=False)
print(text)
