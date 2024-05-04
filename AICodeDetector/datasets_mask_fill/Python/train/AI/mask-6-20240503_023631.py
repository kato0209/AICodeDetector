import torch
from torch_geometric.nn import GCNConv
import torch.nn.functional as F
from torch_geometric.datasets import Planetoid

# <extra_id_0> GNN with two Graph Convolutional layers
class GCN(torch.nn.Module):
    def __init__(self, num_features, num_classes):
        super(GCN, self).__init__()
 <extra_id_1>   <extra_id_2>  self.conv1 = GCNConv(num_features, 16)
        self.conv2 = GCNConv(16, num_classes)

    def <extra_id_3>    <extra_id_4>   x, edge_index = data.x, data.edge_index

 <extra_id_5>      x = self.conv1(x, edge_index)
        x = <extra_id_6>       x = F.dropout(x, training=self.training)
        x = <extra_id_7>       <extra_id_8> F.log_softmax(x,