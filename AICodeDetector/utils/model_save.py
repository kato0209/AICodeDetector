import torch
import os
from datetime import datetime
import logging

def model_save(model):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    save_path = './saved_model'
    os.makedirs(save_path, exist_ok=True)

    # Save the model
    model_save_path = os.path.join(save_path, f'model_{timestamp}.pth')
    torch.save(model.state_dict(), model_save_path)
    logging.info(f"Model saved to {model_save_path}")

def similarity_model_save(model):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    save_path = './saved_model'
    os.makedirs(save_path, exist_ok=True)

    # Save the model
    model_save_path = os.path.join(save_path, f'model_sm_{timestamp}.pth')
    torch.save(model.state_dict(), model_save_path)
    logging.info(f"Model saved to {model_save_path}")