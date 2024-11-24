import torch
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
import torch.nn.functional as F

def top_p_sampling(logits, tokenizer, top_p=0.95, temperature=1.0, top_k=5):
    # 温度でスケーリング
    logits = logits / temperature

    # 確率を降順にソート
    sorted_logits, sorted_indices = torch.sort(logits, descending=True, dim=-1)

    # 次のトークン候補を表示
    top_tokens = [tokenizer.decode(sorted_indices[0, i].item()) for i in range(top_k)]

    # 累積確率を計算
    cumulative_probs = torch.cumsum(sorted_logits, dim=-1)

    # top_pを超えるトークンをフィルタリング
    sorted_indices_to_remove = cumulative_probs > top_p
    # 最初のトークンは残す
    sorted_indices_to_remove[..., 1:] = sorted_indices_to_remove[..., :-1].clone()
    sorted_indices_to_remove[..., 0] = 0

    indices_to_remove = sorted_indices_to_remove.scatter(1, sorted_indices, sorted_indices_to_remove)
    logits[indices_to_remove] = -float("Inf")

    probs = F.softmax(logits, dim=-1)

    # トークンをサンプリング
    next_token = torch.multinomial(probs, num_samples=1).squeeze(1)
    return next_token

def rewrite_code(codes, model, tokenizer, batch_size):
    y = [[] for _ in range(batch_size)]
    state = [[] for _ in range(batch_size)]

    rewrite_codes = []
    
    temperature = 1.0
    top_p = 0.95
    max_length = 128

    prompt_str = "Revise the code with your best effort"
    prefix = ". No need to explain. Just write code(No code comments needed):"
    
    with torch.no_grad():
        for i in range(len(codes)):
            input_prompt = f"{prompt_str}: \"{codes[i]}\" {prefix}"
            inputs = tokenizer(input_prompt, return_tensors="pt")
            input_ids = inputs.input_ids.to(0)
            attention_mask = inputs.attention_mask[0].to(0).unsqueeze(0)

            output_ids = input_ids.clone()
            j = 0
            output_sentence = tokenizer.decode(input_ids[0], skip_special_tokens=True).rstrip()
            print(f"入力コード: {output_sentence}")

            for t in range(max_length):
                # モデルの順伝播
                outputs = model(input_ids=output_ids, attention_mask=attention_mask)
                next_token_logits = outputs.logits[:, -1, :]
                
                # トップpサンプリングで次のトークンを取得
                next_token = top_p_sampling(next_token_logits, tokenizer, top_p=top_p, temperature=temperature)
                next_token = next_token.unsqueeze(-1)
                # 状態を保存
                state[i].append(output_ids.clone())
                
                # 次のトークンを出力に追加
                output_ids = torch.cat([output_ids, next_token], dim=-1)
                attention_mask = torch.cat([attention_mask, torch.tensor([[1]]).to(0)], dim=-1)
                
                # 出力トークンを保存
                y[i].append(next_token)
                
                # EOSトークンで終了
                if next_token.item() == tokenizer.eos_token_id:
                    print("EOSトークン")
                
                j += 1
                print(f"サンプリングステップ {t}: トークンID {next_token.item()}")
            
            # トークン列をデコード
            if len(y[i]) == 0:
                rewrite_codes.append("")
                continue
            
            output_tokens = torch.cat(y[i], dim=-1)
            #print(f"生成されたトークン: {output_tokens}")
            output_sentence = tokenizer.decode(output_tokens[0], skip_special_tokens=True).rstrip()
            print(f"生成されたコード: {output_sentence}")
            rewrite_codes.append(output_sentence)
        
    return rewrite_codes, y, state

def rewrite_code_z(codes, model, tokenizer, batch_size):
    y = [[] for _ in range(batch_size)]
    state = [[] for _ in range(batch_size)]

    rewrite_codes = []

    prompt_str = "Please remove all comments from the Python code shown below. However, please keep the behavior and structure of the code intact, and remove only the comments completely. Do not make any changes to other elements such as functions, methods, variable names, etc.\n Output the code after comment deletion behind Output.\n"

    prefix = "\n Output:\n"
    
    #with torch.distributed.fsdp.FullyShardedDataParallel.summon_full_params(model, offload_to_cpu=True):
    with torch.no_grad():
        for i in range(len(codes)):
            input_prompt = f"{prompt_str}{codes[i]}{prefix}"
            inputs = tokenizer(input_prompt, return_tensors="pt")
            input_ids = inputs.input_ids.to(0)
            attention_mask = inputs.attention_mask[0].to(0).unsqueeze(0)
            output_sentence = tokenizer.decode(input_ids[0], skip_special_tokens=True).rstrip()
            print(f"入力コード: {output_sentence}")
            
            outputs = model.generate(input_ids, attention_mask=attention_mask, do_sample=False, max_new_tokens=128)
            response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)


            rewrite_codes.append(response_text)
        
    return rewrite_codes, y, state

import re
def rewrite_code2(model, batch, args, local_rank, tokenizer):
    y = [[] for _ in range(args["batch_size"])]
    state = [[] for _ in range(args["batch_size"])]
    target_token_log_probs = [[] for _ in range(args["batch_size"])]

    rewrite_codes = []
    batch_input_ids = batch['input_ids'].to(local_rank)
    batch_attention_mask = batch['attention_mask'].to(local_rank)
    original_codes = batch['codes']
    
    temperature = 0.1
    top_p = 0.95
    max_length = 128
    
    for i in range(len(batch_input_ids)):
        input_ids = batch_input_ids[i].unsqueeze(0)
        attention_mask = batch_attention_mask[i].unsqueeze(0)
        output_ids = input_ids.clone()
        j = 0
        output_sentence = tokenizer.decode(input_ids[0], skip_special_tokens=True).rstrip()
        print(f"入力コード: {output_sentence}")

        for t in range(max_length):
            # モデルの順伝播
            outputs = model(input_ids=output_ids, attention_mask=attention_mask)
            next_token_logits = outputs.logits[:, -1, :]

            # トップpサンプリングで次のトークンを取得
            next_token = top_p_sampling(next_token_logits, top_p=top_p, temperature=temperature)

            # ログ確率を計算して保存
            last_token_logits = outputs.logits[0, -1, :]
            log_probs = torch.nn.functional.log_softmax(last_token_logits, dim=-1)
            target_token_log_prob = log_probs[next_token]

            target_token_log_probs[i].append(target_token_log_prob)
            print(target_token_log_prob)

            # 状態を保存
            state[i].append(output_ids.clone())
            
            # 次のトークンを出力に追加
            output_ids = torch.cat([output_ids, next_token], dim=-1)
            attention_mask = torch.cat([attention_mask, torch.tensor([[1]]).to(local_rank)], dim=-1)
            
            # 出力トークンを保存
            y[i].append(next_token)
            
            # EOSトークンで終了
            if next_token.item() == tokenizer.eos_token_id:
                print("EOSトークンで終了")
                break
            
            j += 1
            print(f"サンプリングステップ {t}: トークンID {next_token.item()}")
        
        # トークン列をデコード
        if len(y[i]) == 0:
            rewrite_codes.append("")
            continue
        
        output_tokens = torch.cat(y[i], dim=-1)
        output_sentence = tokenizer.decode(output_tokens[0], skip_special_tokens=True).rstrip()
        print(f"生成されたコード: {output_sentence}")
        rewrite_codes.append(output_sentence)
        
    return rewrite_codes, target_token_log_probs


def calc_similarity_cutom(sentence_model, sentence_model_tokenizer, original_codes, perturbed_codes):
        input_ids = []
        attention_mask = []
        for i in range(len(original_codes)):
            encoded_inputs = sentence_model_tokenizer(original_codes[i], padding="max_length", return_tensors="pt", truncation=True, max_length=128)
            input_ids.append(encoded_inputs.input_ids)
            attention_mask.append(encoded_inputs.attention_mask)
        input_ids = torch.cat(input_ids, dim=0)
        attention_mask = torch.cat(attention_mask, dim=0)
        
        input_ids_p = []
        attention_mask_p = []
        for i in range(len(perturbed_codes)):
            encoded_inputs = sentence_model_tokenizer(perturbed_codes[i], padding="max_length", return_tensors="pt", truncation=True, max_length=128)
            input_ids_p.append(encoded_inputs.input_ids)
            attention_mask_p.append(encoded_inputs.attention_mask)
        
        input_ids_p = torch.cat(input_ids_p, dim=0)
        attention_mask_p = torch.cat(attention_mask_p, dim=0)
        
        with torch.no_grad():
            embeddings1 = sentence_model.output_embeddings(input_ids, attention_mask)
            embeddings2 = sentence_model.output_embeddings(input_ids_p, attention_mask_p)
        similarity_scores = sentence_model.sim(embeddings1, embeddings2)
        return similarity_scores

def create_state_y(batch, args, tokenizer):
    y = [[] for _ in range(args["batch_size"])]
    state = [[] for _ in range(args["batch_size"])]

    batch_input_ids = batch['input_ids']

    rewrite_codes = batch['rewrite_codes']
    batch_input_ids = batch['input_ids']

    i = 0
    for code in rewrite_codes:
        base_prompt = batch_input_ids[i].unsqueeze(0)[0]
        input_ids = tokenizer(code, return_tensors='pt', max_length=128, padding='max_length', truncation=True)['input_ids']
        input_ids = input_ids.squeeze() 

        output_ids = base_prompt
        for token_id in input_ids:
            state[i].append(output_ids)
            y[i].append(token_id.unsqueeze(0).item())
            output_ids = torch.cat([output_ids, token_id.unsqueeze(0)], dim=-1)
        
        i += 1
        
    #print(f"state: {state}")
    return y, state
            
