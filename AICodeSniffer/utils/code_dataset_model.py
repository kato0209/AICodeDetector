from torch.utils.data import Dataset
import os
import torch

class CodeDataset(Dataset):
    def __init__(self, directory_path, tokenizer):
        self.samples = []
        self.tokenizer = tokenizer

        # humanのコードを収集
        human_code_dir = os.path.join(directory_path, 'human')
        for filename in os.listdir(human_code_dir):
            with open(os.path.join(human_code_dir, filename), 'r') as f:
                code = f.read()
                self.samples.append((code, 0))

        # chatGPTのコードを収集
        AI_code_dir = os.path.join(directory_path, 'AI')
        for filename in os.listdir(AI_code_dir):
            with open(os.path.join(AI_code_dir, filename), 'r') as f:
                code = f.read()
                self.samples.append((code, 1))
            
    
    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):
        code, label = self.samples[index]
        inputs = self.tokenizer.encode_plus(code, padding='max_length', max_length=512, truncation=True)
        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']
        #return {'input_ids': torch.tensor(input_ids, dtype=torch.long), 'attention_mask': torch.tensor(attention_mask, dtype=torch.float), 'labels': torch.tensor(label, dtype=torch.float)}
        return {'input_ids': torch.tensor(input_ids, dtype=torch.long), 'attention_mask': torch.tensor(attention_mask, dtype=torch.long), 'labels': torch.tensor(label, dtype=torch.long)}
