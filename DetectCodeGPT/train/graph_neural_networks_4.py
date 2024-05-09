import torch
from data_loader import load_data
from gnn_model import GNN
from torch_geometric.datasets import Planetoid

def load_data(dataset_name="Cora"):
    dataset = Planetoid(root='/tmp/' + dataset_name, name=dataset_name)
    return dataset

dataset = load_data()
data = dataset[0]

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = GNN(dataset.num_node_features, dataset.num_classes).to(device)
data = data.to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01, weight_decay=5e-4)

model.train()
for epoch in range(200):
    optimizer.zero_grad()
    out = model(data)
    loss = torch.nn.functional.nll_loss(out[data.train_mask], data.y[data.train_mask])
    loss.backward()
    optimizer.step()
    print(f'Epoch {epoch+1}, Loss: {loss.item()}')
