import torch
from data_loader import load_data
from gnn_model import GNN
from torch_geometric.datasets import Planetoid

def run(dataset_name):   dataset = Planetoid(root='/tmp/' + dataset_name, name=dataset_name)
    def train():
   batch_size = load_data()
data = dataset[0]

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = GNN(dataset.num_node_features, dataset.num_classes).to(device)
data = data.to(device)

model.eval()
_, pred = model(data).max(dim=1)
correct = int(pred[data.test_mask].eq(data.y[data.test_mask]).sum().item())
accuracy = correct / int(data.test_mask.sum())
print(f'Accuracy: {accuracy}')
