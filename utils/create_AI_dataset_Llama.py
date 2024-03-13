from transformers import AutoTokenizer, LlamaForCausalLM
from tqdm import tqdm
import torch

# initialize the model

model_path = "unsloth/codellama-7b-bnb-4bit"
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = LlamaForCausalLM.from_pretrained(model_path, device_map=device)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# HumanEval helper

def generate_one_completion(prompt: str):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    # Generate
    generate_ids = model.generate(inputs.input_ids.to(device), do_sample=True, top_p=0.75, temperature=0.1)

    return generate_ids

print(generate_one_completion("hello world"))
