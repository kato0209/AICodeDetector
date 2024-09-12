import torch
import torch.distributed as dist
import torch.nn as nn
from torch.nn.parallel import DistributedDataParallel as DDP
import transformers
import os
import sys

from huggingface_hub import login
import os

token = os.getenv("HUGGINGFACE_TOKEN")
login(token=token) 

device = "cuda"  # Adjust based on your setup

def load_model(model_name, model_config):
    quant_config = transformers.BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type='nf4',
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.bfloat16
    )
    tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token
    model = transformers.AutoModelForCausalLM.from_pretrained(
        model_name, 
        trust_remote_code=True, 
        quantization_config=quant_config, 
        device_map="auto", 
        torch_dtype=torch.float32
    )
    
    # Load sentence model
    sentence_model_tokenizer = transformers.AutoTokenizer.from_pretrained('microsoft/graphcodebert-base')
    sentence_model = transformers.AutoModel.from_pretrained('microsoft/graphcodebert-base').to(device)
    
    model_config['tokenizer'] = tokenizer
    model_config['model'] = model
    model_config['sentence_model'] = sentence_model
    model_config['sentence_model_tokenizer'] = sentence_model_tokenizer
    
    return model_config

def setup_ddp(local_rank):
    dist.init_process_group(backend="nccl")
    torch.cuda.set_device(local_rank)

def load_distributed_model(model_name, model_config, local_rank):
    model_config = load_model(model_name, model_config)
    
    # Wrap the model with DDP
    model = model_config['model'].to(local_rank)
    model = DDP(model, device_ids=[local_rank])
    model_config['model'] = model

    sentence_model = model_config['sentence_model'].to(local_rank)
    sentence_model = DDP(sentence_model, device_ids=[local_rank])
    model_config['sentence_model'] = sentence_model
    
    return model_config

def demo_basic(local_rank, local_world_size):
    model_config = {}
    model_name = "meta-llama/Meta-Llama-3.1-70B-Instruct"
    
    # Load the model using DDP
    model_config = load_distributed_model(model_name, model_config, local_rank)
    
    print(f"Model loaded on rank {local_rank}!")

def spmd_main(local_world_size, local_rank):
    setup_ddp(local_rank)
    
    # Call your model demo or training loop
    demo_basic(local_rank, local_world_size)
    
    # Clean up
    dist.destroy_process_group()

if __name__ == "__main__":
    local_world_size = int(os.environ["LOCAL_WORLD_SIZE"])
    local_rank = int(os.environ["LOCAL_RANK"])

    spmd_main(local_world_size, local_rank)
