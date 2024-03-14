import torch.nn as nn
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5-small")
model = AutoModelForSequenceClassification.from_pretrained("Salesforce/codet5-small")

print(model)
