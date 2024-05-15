Input: seq_lengths: a list of integers, where each element is the length of each sequence, and each element is the length of the i-th sequence. The i-th element is the length of the sequence. input_initial_h: initial h value for the cell name: name of the module Returns: A tuple (outputs, output_h), where: outputs: A list of the same length as decoder_inputs of the module.
Output: output_h: H-value returned by the module.
If called with an argument:
  - name: name of the module
  - outputs = list of parameters, a list of integers, where i is the length of outputs (sequence) and outputs is the length of input-outputs.
  - output_h = h value returned by the module.
How to call:
  - name: name of the module