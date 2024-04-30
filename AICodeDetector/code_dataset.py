from torch.utils.data import Dataset
import os
import torch
from masking import tokenize_and_mask
from preprocessing import preprocess_and_save
from load_model import load_mask_filling_model
from filling_mask import replace_masks
from extract_fill import extract_fills, apply_extracted_fills

class CodeDataset(Dataset):
    def __init__(self, directory_path, model_config, args):
        self.samples = []
        self.model_config = model_config
        self.args = args

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

    """
    def __getitem__(self, index):
        code, label = self.samples[index]
        # Tokenize and mask
        inputs = self.model_config["mask_tokenizer"].encode_plus(code, padding='max_length', max_length=512, truncation=True)
        masked_inputs = tokenize_and_mask(inputs['input_ids'], buffer_size=1, span_length=2, pct=0.3, ceil_pct=False)
        # Fill the masks
        raw_fills = replace_masks([masked_inputs], self.model_config, self.args)
        extracted_fills = extract_fills(raw_fills)
        perturbed_texts = apply_extracted_fills([masked_inputs], extracted_fills)

        # Prepare final input
        filled_input_ids = self.model_config["mask_tokenizer"].encode_plus(perturbed_texts[0], padding='max_length', max_length=512, truncation=True)['input_ids']
        attention_mask =self.model_config["mask_tokenizer"].encode_plus(perturbed_texts[0], padding='max_length', max_length=512, truncation=True)['attention_mask']

        return {
            'input_ids': torch.tensor(filled_input_ids, dtype=torch.long),
            'attention_mask': torch.tensor(attention_mask, dtype=torch.long),
            'labels': torch.tensor(label, dtype=torch.long)
        }
    """
    