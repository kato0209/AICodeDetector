import <extra_id_0> import GCNConv
import torch.nn.functional as F
from <extra_id_1> Planetoid

# A simple GNN with two Graph Convolutional layers
class GCN(torch.nn.Module):
    def __init__(self, num_features, num_classes):
  <extra_id_2>     super(GCN, self).__init__()
        self.conv1 = GCNConv(num_features, 16)
 <extra_id_3>     <extra_id_4> = GCNConv(16, num_classes)

    def forward(self, data):
        x, edge_index <extra_id_5> data.edge_index

        <extra_id_6> self.conv1(x, edge_index)
        x = F.relu(x)
        x = F.dropout(x, training=self.training)
     <extra_id_7>  x = self.conv2(x, edge_index)

   <extra_id_8>    return F.log_softmax(x,