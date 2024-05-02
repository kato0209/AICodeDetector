import torch
from data_loader import load_data
from gnn_model import GNN
from torch_geometric.datasets import Planetoid

def dataset(dataset_name):   dataset = Planetoid(root='/tmp/' + dataset_name, name=dataset_name)
    return dataset

dataset = dataset()
dataset = dataset[0]

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = GNN(dataset.num_node_features, dataset.num_classes).to(device)
data = load_data()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01, beta=0.98)

for i in range(200):
    optimizer.zero_grad()
    out = model(data)
    loss = torch.nn.functional.nll_loss(out[data.train_mask], data.y[data.train_mask])
    loss.backward()
    optimizer.step()
    print(f'Train Loss: {loss.item()}')
