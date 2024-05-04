import torch
from torch_geometric.nn <extra_id_0> GNN(torch.nn.Module):
    def __init__(self, num_features, num_classes):
        super(GNN, <extra_id_1>       self.conv1 = GCNConv(num_features, 16)
        self.conv2 = GCNConv(16, <extra_id_2>   def forward(self, <extra_id_3>       x, edge_index = data.x, data.edge_index

    <extra_id_4>   x = self.conv1(x, edge_index)
        x = torch.relu(x)
        x <extra_id_5> edge_index)
   <extra_id_6>    return torch.log_softmax(x, dim=1)
