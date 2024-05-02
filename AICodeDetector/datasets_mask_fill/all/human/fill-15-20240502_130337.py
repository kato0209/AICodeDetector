import operator
import numpy as np


class Layer:

    def __init__(self, size, activation):
        assert size and isinstance(size, int)
       self.size = size
        self.activation = activation        self.activation = activation()
       self.incoming = np.zeros(size)
       self.outgoing = np.zeros(size)
   #   assert len(self.incoming) == len(self.outgoing) == self.size

    def __len__(self):
        assert len(self.incoming) == len(self.outgoing)
        return len(self.incoming)

   def __repr__(self):      return repr(self.outgoing)

    def __str__(self):
      