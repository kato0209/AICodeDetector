from tokenizer import tokenizer
from masking import tokenize_and_mask
from preprocessing import preprocess_and_save
from load_model import load_mask_filling_model
from filling_mask import replace_masks
from extract_fill import extract_fills, apply_extracted_fills
from code_dataset import CodeDataset
from model import CustomBertModel
import argparse
import torch
from torch.utils.data import DataLoader, random_split
from transformers.optimization import AdamW, get_linear_schedule_with_warmup
from utils.model_save import model_save
from utils.confusion_matrix import plot_confusion_matrix

import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from datetime import datetime
import logging
from sklearn.metrics import classification_report, confusion_matrix


log_path = './logs'
os.makedirs(log_path, exist_ok=True)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
logging.basicConfig(filename=os.path.join(log_path, f'test_{timestamp}.log'),
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)


label_list = [0, 1, 0, 1, 0, 1, 0, 1]
pred_list = [0, 1, 0, 0, 0, 1, 0, 1]
target_names = ['ChatGPT','Human']
logging.info('Confusion Matrix')
logging.info('Classification Report')
cm = confusion_matrix(label_list, pred_list)
plot_confusion_matrix(cm, target_names, title='Confusion Matrix')
logging.info(classification_report(label_list, pred_list, target_names=target_names))
