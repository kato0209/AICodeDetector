from loguru import logger
import random
from tqdm import tqdm
import re

def extract_function_definitions(prompt):
    pattern = r"def\s+\w+\s*\(.*?\):"
    matches = re.findall(pattern, prompt)
    return matches

def generate_data(max_num=1000, min_len=0, max_len=128, max_comment_num=10, max_def_num=5, cut_def=False, max_todo_num=3, path=None):

    logger.info(f'Loading data from {path}')
    import json
    all_originals = []
    all_samples = []  # machine generated

    min_len_count = 0

    with open(path, 'r') as f:
        for line in tqdm(f, ncols=70):
            line = line.strip()
            if line == '':
                continue
            line = json.loads(line)

            def_str = extract_function_definitions(line['prompt'])

            # avoid examples that are too short (less than min_len words)
            # around 2000/100000 examples have around 55 words
            if len(line['solution'].split()) < min_len or len(line['output'].split()) < min_len:
                min_len_count += 1
                continue

            # cut to 128 tokens
            # def_strを先頭にくっつける

            line['solution'] = ' '.join(def_str) + ' ' + ' '.join(line['solution'].split(' '))
            line['output'] = ' '.join(def_str) + ' ' + ' '.join(line['output'].split(' '))

            all_originals.append(' '.join(line['solution'].split(' ')[:max_len]))
            all_samples.append(' '.join(line['output'].split(' ')[:max_len]))

    all_samples = random.sample(all_samples, 70)

    data = {
        "original": all_originals,
        "sampled": all_samples
    }

    return data
