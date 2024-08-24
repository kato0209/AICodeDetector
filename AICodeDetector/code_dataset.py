from torch.utils.data import Dataset
import os
import torch
from masking import tokenize_and_mask
from preprocessing import preprocess_and_save
from load_model import load_mask_filling_model
from filling_mask import replace_masks
from extract_fill import extract_fills, apply_extracted_fills
from masking import tokenize_and_mask

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
        return {'code': code, 'labels': torch.tensor(label, dtype=torch.long)}

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


class CodeDatasetCS(Dataset):
    def __init__(self, data, model_config, args):
        self.samples = []
        self.model_config = model_config
        self.args = args

        # humanのコードを収集
        for code in data["original"]:
            self.samples.append((code, 0))

        """"
        # chatGPTのコードを収集
        for code in data["sampled"]:
            self.samples.append((code, 1))       
        """  
            
    
    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):
        code, label = self.samples[index]
        inputs = self.model_config["tokenizer"](code, padding='max_length', return_tensors="pt", truncation=True, max_length=128)
        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']
        #return {'input_ids': torch.tensor(input_ids, dtype=torch.long), 'attention_mask': torch.tensor(attention_mask, dtype=torch.float), 'labels': torch.tensor(label, dtype=torch.float)}
        return {'input_ids': torch.tensor(input_ids, dtype=torch.long), 'attention_mask': torch.tensor(attention_mask, dtype=torch.long), 'labels': torch.tensor(label, dtype=torch.long)}

class CodeDatasetFromCodeSearchNet(Dataset):
    def __init__(self, data, model_config, args, perturb=False):
        self.samples = []
        self.model_config = model_config
        self.args = args
        self.perturb = perturb

        if perturb: 
            for code, perturb_code in data["original"]:
                self.samples.append((code, perturb_code, 0, 0))
    
            for code, perturb_code, sub_label in data["sampled"]:
                self.samples.append((code, perturb_code, 1, sub_label))
        else:
            for code in data["original"]:
                self.samples.append((code, 0, 0))
        
            for code, sub_label in data["sampled"]:
                self.samples.append((code, 1, sub_label))
    
    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):

        if not self.perturb:
            code, label, sub_label = self.samples[index]
            inputs = self.model_config["tokenizer"].encode_plus(code, padding='max_length', max_length=128, truncation=True)
            input_ids = inputs['input_ids']
            attention_mask = inputs['attention_mask']
            return {'input_ids': torch.tensor(input_ids, dtype=torch.long), 'attention_mask': torch.tensor(attention_mask, dtype=torch.long), 'labels': torch.tensor(label, dtype=torch.long), 'sub_label': torch.tensor(sub_label, dtype=torch.long)}
        else:
            code, perturb_code, label, sub_label = self.samples[index]
            inputs = self.model_config["tokenizer"].encode_plus(code, padding='max_length', max_length=128, truncation=True)
            input_ids = inputs['input_ids']
            attention_mask = inputs['attention_mask']
            
            perturb_inputs = self.model_config["tokenizer"].encode_plus(perturb_code, padding='max_length', max_length=128, truncation=True)
            perturb_input_ids = perturb_inputs['input_ids']
            perturb_attention_mask = perturb_inputs['attention_mask']
            #return {'input_ids': torch.tensor(input_ids, dtype=torch.long), 'attention_mask': torch.tensor(attention_mask, dtype=torch.float), 'labels': torch.tensor(label, dtype=torch.float)}
            return {
                'input_ids': torch.tensor(input_ids, dtype=torch.long), 
                'attention_mask': torch.tensor(attention_mask, dtype=torch.long), 
                'labels': torch.tensor(label, dtype=torch.long),
                'perturb_input_ids': torch.tensor(perturb_input_ids, dtype=torch.long),
                'perturb_attention_mask': torch.tensor(perturb_attention_mask, dtype=torch.long),
                'sub_label': torch.tensor(sub_label, dtype=torch.long),
                "original_code": code,
                "perturb_code": perturb_code
            }

class CodeDatasetRewriting(Dataset):
    def __init__(self, data, model_config, args):
        self.samples = []
        self.args = args
        self.model_config = model_config

        human_data = data["human"]
        ai_data = data["ai"]

        for i in range (len(human_data["original"])):
            #self.samples.append((human_data["original"][i], human_data["rewrite"][i], 0))
            self.samples.append((human_data["original"][i], 0, 0))
        
        for i in range (len(ai_data["original"])):
            #self.samples.append((ai_data["original"][i], ai_data["rewrite"][i], 1))
            self.samples.append((ai_data["original"][i], 0, 1))
    
    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):

        code, rewrite_code, label = self.samples[index]
        input = f"original: {code} \ rewrite: {rewrite_code}"
        inputs = self.model_config["tokenizer"].encode_plus(code, padding='max_length', max_length=300, truncation=True)
        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']
        
        return {'input_ids': torch.tensor(input_ids, dtype=torch.long), 'attention_mask': torch.tensor(attention_mask, dtype=torch.long), 'labels': torch.tensor(label, dtype=torch.long), 'code': code, 'rewrite_code': rewrite_code}

class CodeDatasetSimilarity(Dataset):
    def __init__(self, data, args):
        self.samples = []
        self.args = args

        human_data = data["human"]
        ai_data = data["ai"]

        for i in range (len(human_data["original"])):
            self.samples.append((human_data["original"][i], human_data["rewrite"][i], 0))
        
        for i in range (len(ai_data["original"])):
            self.samples.append((ai_data["original"][i], ai_data["rewrite"][i], 1))
    
    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):

        code, rewrite_code, label = self.samples[index]
        
        return {'code': code, 'rewrite_code': rewrite_code, 'labels': torch.tensor(label, dtype=torch.long)}

class CodeDatasetForLLM(Dataset):
    def __init__(self, data, args):
        self.samples = []

        masked_original = []
        masked_sampled = []
        for i in range(len(data["original"])):
            masked_original.append(tokenize_and_mask(data["original"][i], buffer_size=args.buffer_size, span_length=args.span_length, pct=args.pct_words_masked))
            masked_sampled.append(tokenize_and_mask(data["sampled"][i], buffer_size=args.buffer_size, span_length=args.span_length, pct=args.pct_words_masked))
        
        for i in range(len(data["original"])):
            self.samples.append((data["original"][i], masked_original[i], 0))
    
        for i in range(len(data["sampled"])):
            self.samples.append((data["sampled"][i], masked_sampled[i], 1))
    
    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):
        code, masked_code, label = self.samples[index]
        return {'code': code, 'masked_code': masked_code, 'labels': torch.tensor(label, dtype=torch.long)}
