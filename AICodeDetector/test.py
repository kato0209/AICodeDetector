from openai import OpenAI
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

from loguru import logger
from tqdm import tqdm

from masking import tokenize_and_mask
from preprocessing import preprocess_and_save
from load_model import load_mask_filling_model
from filling_mask import replace_masks
from extract_fill import extract_fills, apply_extracted_fills
from code_dataset import CodeDataset
import argparse
import torch
import os
import datetime
from torch.utils.data import DataLoader, random_split
import ast

def query_chatgpt_and_save(prompt, api_key, file_path, extension="py", model="gpt-4o", temperature=0.2):
    client = OpenAI()
    OpenAI.api_key = api_key

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=128,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    response_text = response.choices[0].message.content

    return response_text


# APIキー（ここにあなたのAPIキーを入れる）
api_key = os.environ['OPENAI_API_KEY']

prompt = """

        Generate the following Python code rewrite according to your idea.
        Please do not output anything other than the rewritten Python code.
        Please do not output the exact same source code as the input.\n

        {code}\n
        
        OUTPUT:\n

        """

code = """
def absfile(path, where=None):
    if os.path.isabs(path):
        return os.path.normpath(path)
    if where is not None:
        full_path = os.path.join(os.path.abspath(where), path)
        if os.path.isfile(full_path):
            return os.path.normpath(full_path)
    return None


def read_file(path, mode='r'):
    #Read a file, returning its contents as a string. If the file can't be found,
    return None.
    
    full_path = absfile(path
"""

input_prompt = prompt.format(code=code)

response_text = query_chatgpt_and_save(input_prompt, api_key, "", "", temperature=0.2)
print(response_text)
