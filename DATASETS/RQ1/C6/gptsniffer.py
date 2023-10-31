# -*- coding: utf-8 -*-
"""GPTSniffer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uVIHvwPMTclqbQ3TGJftMwddMqiAYhYz
"""

#!pip install torch transformers pandas
# !pip install Keras-Preprocessing

import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from torch.utils.data import DataLoader, Dataset
from sklearn.metrics import confusion_matrix
import os
os.environ["OMP_NUM_THREADS"] = "1" # export OMP_NUM_THREADS=1
os.environ["OPENBLAS_NUM_THREADS"] = "1" # export OPENBLAS_NUM_THREADS=1 
os.environ["MKL_NUM_THREADS"] = "1" # export MKL_NUM_THREADS=1
os.environ["VECLIB_MAXIMUM_THREADS"] = "1" # export VECLIB_MAXIMUM_THREADS=1

import pandas as pd
import numpy as np
#from timm.optim.lion import Lion
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

#from google.colab import drive
#drive.mount('/content/drive/',force_remount=False)
#DATA_PATH = '/content/drive/My Drive/Colab Notebooks/SourceSniffer/'
DATA_PATH = './CONF'
from os.path import join

# Set the directory where the training and testing data is stored
train_data_path = join(DATA_PATH,'training_data')
test_data_path = join(DATA_PATH,'testing_data') 


# Set device to GPU if available, otherwise use CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#device = torch.device('cpu')

# Define the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModelForSequenceClassification.from_pretrained("microsoft/codebert-base")



# define the dataset
class CodeDataset(Dataset):
    def __init__(self, directory):
        self.samples = []
        for filename in os.listdir(directory):
            label = int(filename.split('_')[0])
            with open(os.path.join(directory, filename), 'r') as f:
                code = f.read()
                self.samples.append((code, label))
    
    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):
        code, label = self.samples[index]
        inputs = tokenizer.encode_plus(code, padding='max_length', max_length=512, truncation=True)
        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']
        return {'input_ids': torch.tensor(input_ids, dtype=torch.long), 'attention_mask': torch.tensor(attention_mask, dtype=torch.long), 'labels': torch.tensor(label, dtype=torch.long)}


def get_code_without_comments(filepath):
    with open(filepath, 'rb') as f:
        lines = f.readlines()
    code_lines = []
    for line in tokenize.tokenize(lines.__iter__().__next__):
        if line.type != tokenize.COMMENT:
            code_lines.append(line.string)
    return ''.join(code_lines)

"""Something goes here."""

# Define the training dataset and dataloader
train_dataset = CodeDataset(train_data_path)
train_dataloader = DataLoader(train_dataset, batch_size=32, shuffle=True)

# Define the testing dataset and dataloader
test_dataset = CodeDataset(test_data_path)
test_dataloader = DataLoader(test_dataset, batch_size=32, shuffle=False)

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

from sklearn.metrics import confusion_matrix
import time
start = time.time()
#cm = confusion_matrix(y_true, y_pred)
end = time.time()
print(f'time to inference: {end - start} seconds')

#print(cm)




#Plot the confusion matrix. Set Normalize = True/False

def plot_confusion_matrix(cm, classes, normalize=True, title='Confusion matrix', cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.figure(figsize=(20,20))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        cm = np.around(cm, decimals=2)
        cm[np.isnan(cm)] = 0.0
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    

#Print the Target names
from sklearn.metrics import classification_report, confusion_matrix
import itertools 
#shuffle=False
target_names = ['ChatGPT','Human']

print('Confusion Matrix')
cm = confusion_matrix(y_true, y_pred)
plot_confusion_matrix(cm, target_names, title='Confusion Matrix')
# Print Classification Report
print('Classification Report')
print(classification_report(y_true, y_pred, target_names=target_names))
