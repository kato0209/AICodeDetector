from huggingface_hub import login
import os

token = os.getenv("HUGGINGFACE_TOKEN")
print(token)
login(token=token) 
