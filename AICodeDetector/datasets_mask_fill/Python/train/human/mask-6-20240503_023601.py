import operator
import <extra_id_0> np


class Layer:

 <extra_id_1>  def __init__(self, size, activation):
        assert size and isinstance(size, int)
    <extra_id_2>   <extra_id_3> size
 <extra_id_4>      self.activation = activation()
        self.incoming = np.zeros(size)
        self.outgoing = np.zeros(size)
    <extra_id_5>   assert len(self.incoming) == len(self.outgoing) == <extra_id_6>   def __len__(self):
   <extra_id_7>    assert len(self.incoming) == len(self.outgoing)
        return len(self.incoming)

    def __repr__(self):
  <extra_id_8>     return repr(self.outgoing)

    def __str__(self):
      