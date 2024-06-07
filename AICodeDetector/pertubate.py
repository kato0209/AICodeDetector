import re
import transformers
import torch

def rewrite_code(codes, model_config, args):
    prompt = """
    Please first explain the functionality of the python code above. Then generate a possible rewrite for this python code according to your explanation. Please organize all the code in a single markdown code block. Please do not add any clarifications after the rewritten code.
    ```
    {code}
    ```
    """

    tokenizer = model_config['tokenizer']
    model = model_config['model']

    rewrite_codes = []
    for code in codes:
        input_prompt = prompt.format(code=code)
        input_ids = tokenizer(input_prompt, return_tensors="pt", truncation=True, max_length=128).input_ids
        input_ids = input_ids.to(args.DEVICE)
        input_ids_len = len(input_ids[0])
        outputs = model.generate(input_ids, do_sample=True, max_length=128+input_ids_len, top_p=0.95, temperature=0.2, pad_token_id=tokenizer.pad_token_id, use_cache=True)
        decoded_output = tokenizer.decode(outputs[0])
        pattern = r"```(.*?)```"
        rewritten_code = re.findall(pattern, decoded_output, re.DOTALL)
        if rewritten_code:
            rewrite_codes.append(rewritten_code[0].strip())
        else:
            rewrite_codes.append("")
    return rewrite_codes
