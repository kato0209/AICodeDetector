import torch
from data_loader import load_data
from gnn_model import GNN
from torch_geometric.datasets import Planetoid

def <extra_id_0>   dataset = Planetoid(root='/tmp/' + dataset_name, name=dataset_name)
    return dataset

dataset <extra_id_1> = dataset[0]

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = GNN(dataset.num_node_features, dataset.num_classes).to(device)
data <extra_id_2> = torch.optim.Adam(model.parameters(), lr=0.01, <extra_id_3> in range(200):
    optimizer.zero_grad()
    <extra_id_4> model(data)
    loss = torch.nn.functional.nll_loss(out[data.train_mask], data.y[data.train_mask])
    loss.backward()
    optimizer.step()
    <extra_id_5> Loss: {loss.item()}')
