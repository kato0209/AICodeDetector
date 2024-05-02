import torch
from torch_geometric.nn import GCNConv

class GNN(torch.nn.Module):
    def __init__(self, num_features, num_classes):
       <extra_id_0> self).__init__()
       <extra_id_1> = GCNConv(num_features, <extra_id_2>       self.conv2 = GCNConv(16, <extra_id_3>   def forward(self, data):
        x, edge_index = data.x, data.edge_index

        x = self.conv1(x, edge_index)
       <extra_id_4> = torch.relu(x)
        <extra_id_5> self.conv2(x, edge_index)
      <extra_id_6> return torch.log_softmax(x, dim=1)
