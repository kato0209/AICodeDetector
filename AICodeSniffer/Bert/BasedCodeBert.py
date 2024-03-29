import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from torch.utils.data import DataLoader, Dataset
from sklearn.metrics import confusion_matrix
import os
import pandas as pd
import numpy as np
#from timm.optim.lion import Lion
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from torch.utils.data import random_split
import time
from sklearn.metrics import classification_report, confusion_matrix

from os.path import join
from datetime import datetime
import logging

from custom_bert import CustomBertModel

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.model_save import model_save
from utils.code_dataset_model import CodeDataset
from utils.custom_trainer import CustomTrainer
from utils.confusion_matrix import plot_confusion_matrix

# Set device to GPU if available, otherwise use CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#device = torch.device('cpu')

# Define the tokenizer and the model
cbm = CustomBertModel()
#cbm.set_classification_head()
model = cbm.return_model()

# define the dataset
DATASET_PATH = 'datasets/go/train'
datasets = CodeDataset(DATASET_PATH, cbm.tokenizer)

# データセットの全長を取得
dataset_size = len(datasets)
train_size = int(0.8 * dataset_size)
test_size = dataset_size - train_size

# データセットをランダムに分割
train_dataset, test_dataset = random_split(datasets, [train_size, test_size])

train_dataloader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=32, shuffle=False)

log_path = './logs'
os.makedirs(log_path, exist_ok=True)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
logging.basicConfig(filename=os.path.join(log_path, f'training_{timestamp}.log'),
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

# Define the training arguments and the trainer
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=12,
    per_device_train_batch_size=32,
    per_device_eval_batch_size=32,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
    optim='adamw_torch',
    learning_rate=5e-5,
    save_total_limit=2,
    # metric_for_best_model='f1',
    # report_to='wandb',
    # push_to_hub=True,
    # hub_strategy='every_save',
    # hub_model_id=repository_id,
    # hub_token=HfFolder.get_token(),
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset
    # eval_dataset=test_dataset,
)

# Train the model with the pre-defined parameters
trainer.train()


# Test the model and print out the confusion matrix
model.eval()
y_true = []
y_pred = []
start = time.time()
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

end = time.time()

logging.info(f'time to inference: {end - start} seconds')    


target_names = ['ChatGPT','Human']

logging.info('Confusion Matrix')
cm = confusion_matrix(y_true, y_pred)
plot_confusion_matrix(cm, target_names, title='Confusion Matrix')
# Print Classification Report
logging.info('Classification Report')
logging.info(classification_report(y_true, y_pred, target_names=target_names))

model_save(model)
