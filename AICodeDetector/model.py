import torch.nn as nn
from transformers import AutoTokenizer, AutoModel

class CustomClassificationHead(nn.Module):
    def __init__(self,config):
        super(CustomClassificationHead, self).__init__()
        self.N_MSD = 5
        self.dense = nn.Linear(config.hidden_size, config.hidden_size)
        self.dropouts = nn.ModuleList([nn.Dropout(0.2) for _ in range(self.N_MSD)])
        self.regressor = nn.Linear(config.hidden_size, 2)
    
    def forward(self, features, **kwargs):
        # featuresの形状は [batch_size, sequence_length, hidden_size] を想定
        batch_size, sequence_length, hidden_size = features.size()

        # featuresを [batch_size, hidden_size] に変形
        features = features.view(batch_size, -1, hidden_size).mean(dim=1)

        # 線形変換とドロップアウトを適用
        features = self.dense(features)
        logits = sum([self.regressor(dropout(features)) for dropout in self.dropouts]) / self.N_MSD
        return logits

class CustomBertModel(nn.Module):
    def __init__(self):
        super(CustomBertModel, self).__init__()
        self.model = AutoModel.from_pretrained("microsoft/codebert-base")
        self.dropout = nn.Dropout(self.model.config.hidden_dropout_prob)
    
    def set_classification_head(self):
        self.classifier = CustomClassificationHead(self.model.config)
    
    def return_model(self):
        return self.model
    
    def forward(self, input_ids=None, attention_mask=None, labels=None):
        print(2222)
        outputs = self.model(input_ids, attention_mask=attention_mask)
        print(333)
        print(outputs)
        print(outputs.pooler_output)
        pooled_output = pooled = outputs[1]
        print(2444222)
        pooled_output = self.dropout(pooled_output)
        print(6666)
        logits = self.classifier(pooled_output)

        print(1111)
        print(pooled)
        print(pooled_output)
        
        print(logits)

        return outputs


