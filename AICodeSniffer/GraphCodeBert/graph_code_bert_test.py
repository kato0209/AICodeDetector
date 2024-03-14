import os
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.utils.data import DataLoader, Dataset
from sklearn.metrics import accuracy_score
import torch.nn as nn
from datetime import datetime
import logging
from sklearn.metrics import classification_report, confusion_matrix


import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.confusion_matrix import plot_confusion_matrix
from utils.code_dataset_model import CodeDataset

from custom_graph_code_bert import CustomGraphCodeBertModel

# Define the tokenizer and the model
cgm = CustomGraphCodeBertModel()
#cbm.set_classification_head()
model = cgm.return_model()
model_path = 'saved_model/model_20240314_084111.pth' 
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.load_state_dict(torch.load(model_path, map_location=device))
model.to(device)


# define the dataset
#DATASET_PATH = 'datasets/Python/temp_test'
DATASET_PATH = 'datasets/go/train'
datasets = CodeDataset(DATASET_PATH, cgm.tokenizer)
test_dataloader = DataLoader(datasets, batch_size=32, shuffle=False)


log_path = './logs'
os.makedirs(log_path, exist_ok=True)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
logging.basicConfig(filename=os.path.join(log_path, f'test_{timestamp}.log'),
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

model.eval()
y_true = []
y_pred = []
with torch.no_grad():
    for batch in test_dataloader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)
        outputs = model(input_ids, attention_mask=attention_mask)
        logits = outputs.logits
        predictions = torch.argmax(logits, dim=1)
        y_true += labels.tolist()
        y_pred += predictions.tolist()
accuracy = accuracy_score(y_true, y_pred)
print(y_true)
print(y_pred)
print(accuracy)


logging.info(model_path)
target_names = ['ChatGPT','Human']
logging.info('Confusion Matrix')
cm = confusion_matrix(y_true, y_pred)
plot_confusion_matrix(cm, target_names, title='Confusion Matrix')
logging.info('Classification Report')
logging.info(classification_report(y_true, y_pred, target_names=target_names))
