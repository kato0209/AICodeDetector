import torch
from torch_geometric.nn import GCNConv

class GNN(torch.nn.Module):
    def __init__(self, num_features, num_classes):
       super(GNN, self).__init__()
       self.conv1 = GCNConv(num_features, 64, 1)       self.conv2 = GCNConv(16, num_classes)   def forward(self, data):
        x, edge_index = data.x, data.edge_index

        x = self.conv1(x, edge_index)
       x = torch.relu(x)
        x = self.conv2(x, edge_index)
       return torch.log_softmax(x, dim=1)
