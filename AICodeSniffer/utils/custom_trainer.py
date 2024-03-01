
import torch.nn.functional as F
from transformers import Trainer
import torch
import torch.nn as nn

class CustomTrainer(Trainer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ITERS_TO_ACCUMULATE = 2
        self.accumulation_steps = ITERS_TO_ACCUMULATE

    def compute_loss(self, model, inputs, return_outputs=False):
        # Extract the inputs for your loss function
        labels = inputs.get("labels")
        
        # Forward pass
        outputs = model(**inputs)
        logits1 = outputs.logits  # Assuming this is how your model outputs are structured
        outputs = model(**inputs)
        logits2 = outputs.logits  # Assuming this is how your model outputs are structured

        probabilities1 = F.softmax(logits1, dim=1)
        probabilities2 = F.softmax(logits2, dim=1)
        loss = loss_fn(probabilities1, probabilities2, labels.float())
        return (loss, outputs) if return_outputs else loss
    
    def training_step(self, model, inputs):
        model.train()
        inputs = self._prepare_inputs(inputs)

        loss = self.compute_loss(model, inputs, return_outputs=False)

        # ここで累積勾配を適用
        if self.accumulation_steps > 1:
            loss = loss / self.accumulation_steps
        loss.backward()

        if (self.state.global_step + 1) % self.accumulation_steps == 0:
            self.optimizer.step()
            self.optimizer.zero_grad()
            self.lr_scheduler.step()
            self.state.global_step += 1

        return loss
    

def compute_kl_loss(p, q, pad_mask=None):

    p_loss = F.kl_div(F.log_softmax(p, dim=-1), F.softmax(q, dim=-1), reduction='none')
    q_loss = F.kl_div(F.log_softmax(q, dim=-1), F.softmax(p, dim=-1), reduction='none')

    # pad_mask is for seq-level tasks
    if pad_mask is not None:
        p_loss.masked_fill_(pad_mask, 0.)
        q_loss.masked_fill_(pad_mask, 0.)

    # You can choose whether to use function "sum" and "mean" depending on your task
    p_loss = p_loss.sum()
    q_loss = q_loss.sum()

    loss = (p_loss + q_loss) / 2
    return loss

def loss_fn(logits1, logits2, label):
    # RMSE loss
    RDROP_ALPHA = 0.5
    rmse1 = torch.sqrt(nn.MSELoss(reduction='mean')(logits1[:, 1], label))
    rmse2 = torch.sqrt(nn.MSELoss(reduction='mean')(logits2[:, 1], label))

    # R-Drop
    kl_loss = compute_kl_loss(rmse1, rmse2)

    total_loss = (rmse1 + rmse2) / 2 + RDROP_ALPHA * kl_loss
    return total_loss
