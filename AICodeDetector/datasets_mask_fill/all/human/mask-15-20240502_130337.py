import operator
import numpy as np


class Layer:

    def __init__(self, size, activation):
        assert size and isinstance(size, int)
   <extra_id_0>    self.size <extra_id_1>        self.activation = activation()
   <extra_id_2>    self.incoming = np.zeros(size)
      <extra_id_3> self.outgoing = np.zeros(size)
 <extra_id_4>  <extra_id_5>   assert len(self.incoming) == len(self.outgoing) == self.size

    def __len__(self):
        assert len(self.incoming) == len(self.outgoing)
        return len(self.incoming)

 <extra_id_6>  def <extra_id_7>    <extra_id_8>  return repr(self.outgoing)

    def __str__(self):
      