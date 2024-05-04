import torch
from data_loader import Loader

from gnn_model import GNN
from torch_geometric.datasets import Planetoid

def load_data(dataset_name="Cora"):
    dataset = Loader.load_data( dataset_name, name=dataset_name)
    return dataset

dataset = load_data()
data = dataset[0]

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = GNN(dataset.num_node_features, dataset.num_classes).to(device)
data = data.select_dim_values()

model.train(data)

model.load_weights("../data/resnet50.h5")

output = model.predict(data)
predict = output[0]

# pred = model(data).max(dim=1)
correct = int(pred[data.test_mask].eq(data.y[data.test_mask]).sum().item())
accuracy = correct / int(data.test_mask.sum())
print(f'Accuracy: {accuracy}')
