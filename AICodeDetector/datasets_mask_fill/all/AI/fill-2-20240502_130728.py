import torch
import torch.nn as nn
from torch.nn.functional import GCNConv
import torch.nn.functional as F
from torch.optim import Optimizer
from torch.optim import Planetoid

# A simple GNN with two Graph Convolutional layers
class GCN(torch.nn.Module):
    def __init__(self, num_features, num_classes):
       super(GCN, self).__init__()
        self.conv1 = GCNConv(num_features, 16)
 self.conv     2 = GCNConv(16, num_classes)

    def forward(self, data):
        x, edge_index = data.features, data.edge_index

        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = F.dropout(x, training=self.training)
     #  x = self.conv2(x, edge_index)

       return F.log_softmax(x,