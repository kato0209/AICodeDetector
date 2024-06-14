from masking import tokenize_and_mask
from filling_mask import replace_masks
from extract_fill import extract_fills, apply_extracted_fills
from pertubate import rewrite_code

import numpy as np
import scipy.stats

def random_insert_space(text, pct=0.3, mean=1):
    '''
    randomly insert a space for pct of the lines
    '''
    tokens = text.split(' ')
    n_tokens = len(tokens)
    n_inserted = int(n_tokens * pct)
    inserted_idxs = np.random.choice(n_tokens, n_inserted, replace=False)
    for idx in inserted_idxs:
        n_spaces = scipy.stats.poisson.rvs(mean) + 1
        # n_spaces = 1
        tokens[idx] = tokens[idx] + ' '*n_spaces
    return ' '.join(tokens)

def random_insert_newline(text, pct=0.3, mean=1):
    '''
    randomly insert a newline for pct of the lines
    '''
    lines = text.split('\n')
    n_lines = len(lines)
    n_inserted = int(n_lines * pct)
    inserted_idxs = np.random.choice(n_lines, n_inserted, replace=False)
    for idx in inserted_idxs:
        n_newlines = 1
        # n_newlines = scipy.stats.poisson.rvs(mean) + 1
        lines[idx] = lines[idx] + '\n'*n_newlines
    return '\n'.join(lines)

def random_insert_newline_space(text_label_pairs, pct=0.5, lambda_poisson=2):
    texts = [x[0] for x in text_label_pairs]
    perturbed_texts_part1 = [random_insert_space(x, pct, lambda_poisson) for x in texts]
    perturbed_texts_part2 = [random_insert_newline(x, pct, lambda_poisson) for x in texts]
    total_num = len(perturbed_texts_part1)
    n1 = int(total_num / 2)
    n2 = total_num - n1
    perturbed_texts_part1 = perturbed_texts_part1[:n1]
    perturbed_texts_part2 = perturbed_texts_part2[:n2]
    return perturbed_texts_part1 + perturbed_texts_part2

def pertubate_code(codes, model_config, args):
    span_length = 2
    pct = 0.3
    buffer_size = 1
    #masked_text = tokenize_and_mask(tokens, buffer_size, span_length, pct, ceil_pct=False)
    masked_codes = [tokenize_and_mask(x, buffer_size, span_length, pct, ceil_pct=False) for x in codes]

    raw_fills = replace_masks(masked_codes, model_config, args)
    #print(raw_fills)
    extracted_fills = extract_fills(raw_fills)
    #print(extracted_fills)
    perturbed_codes = apply_extracted_fills(masked_codes, extracted_fills)
    #print(perturbed_texts)

    return masked_codes, perturbed_codes 

def pertube_data(data, model_config, args):
    perturbation_type = 'mask'
    new_data = {
        "original": [],
        "sampled": []
    }
    if perturbation_type == 'space-line':
        human_codes_perturbed = random_insert_newline_space(data["original"])
        AI_codes_perturbed = random_insert_newline_space(data["sampled"])
        for i in range(len(data["original"])):
            new_data["original"].append((data["original"][i], human_codes_perturbed[i]))
        
        for i in range(len(data["sampled"])):
            new_data["sampled"].append((data["sampled"][i][0], AI_codes_perturbed[i], data["sampled"][i][1]))

        data = new_data
    elif perturbation_type == 'rewrite':
        batch_size = 16
        all_human_codes = data["original"]
        all_human_rewritten_codes = []
        all_AI_codes = data["sampled"]
        all_AI_rewritten_codes = []

        for i in range(0, len(all_human_codes), batch_size):
            batch_codes = all_human_codes[i:i + batch_size]
            human_rewritten_codes = rewrite_code(batch_codes, model_config, args)
            all_human_rewritten_codes += human_rewritten_codes
        
        for i in range(0, len(all_AI_codes), batch_size):
            batch_codes_pair = all_AI_codes[i:i + batch_size]
            batch_codes = [x[0] for x in batch_codes_pair]
            AI_rewritten_codes = rewrite_code(batch_codes, model_config, args)
            all_AI_rewritten_codes += AI_rewritten_codes
        
        for i in range(len(all_human_codes)):
            new_data["original"].append((all_human_codes[i], all_human_rewritten_codes[i]))
        
        for i in range(len(all_AI_codes)):
            new_data["sampled"].append((all_AI_codes[i][0], all_AI_rewritten_codes[i], all_AI_codes[i][1]))

        data = new_data
    elif perturbation_type == 'mask':
        batch_size = 16
        all_human_codes = data["original"]
        all_human_masked_codes = []
        all_human_perturbed_codes = []

        all_AI_codes = data["sampled"]
        all_AI_masked_codes = []
        all_AI_perturbed_codes = []

        # 各バッチでの処理、拡張子も動的に適用
        for i in range(0, len(all_human_codes), batch_size):
            batch_codes = all_human_codes[i:i + batch_size]
            human_masked_codes, human_perturbed_codes = pertubate_code(batch_codes, model_config, args)
            all_human_masked_codes += human_masked_codes
            all_human_perturbed_codes += human_perturbed_codes
            

        # AIコードの処理も同様に行う
        for i in range(0, len(all_AI_codes), batch_size):
            batch_codes_pair = all_AI_codes[i:i + batch_size]
            batch_codes = [x[0] for x in batch_codes_pair]
            AI_masked_codes, AI_perturbed_codes = pertubate_code(batch_codes, model_config, args)
            all_AI_masked_codes += AI_masked_codes
            all_AI_perturbed_codes += AI_perturbed_codes

        for i in range(len(all_human_codes)):
            new_data["original"].append((all_human_codes[i], all_human_perturbed_codes[i]))
        
        for i in range(len(all_AI_codes)):
            new_data["sampled"].append((all_AI_codes[i][0], all_AI_perturbed_codes[i], all_AI_codes[i][1]))
        data = new_data
    return data
