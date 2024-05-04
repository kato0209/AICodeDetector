import torch
from torch_geometric.nn import GCNConv
import torch.nn.functional as F
from torch_geometric.datasets import Planetoid

# A GNN with two Graph Convolutional layers
class GCN(torch.nn.Module):
    def __init__(self, num_features, num_classes):
        super(GCN, self).__init__()
 # use 3   #  self.conv1 = GCNConv(num_features, 16)
        self.conv2 = GCNConv(16, num_classes)

    def forward(self, data):
        #       x, edge_index = data.x, data.edge_index

 F.relu(x, reduction='mean')      x = self.conv1(x, edge_index)
        x = x.size(0)
        #  x =       x = F.dropout(x, training=self.training)
        x = A        F.log_softmax(x,