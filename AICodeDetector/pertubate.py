import re
import transformers

def rewrite_code(codes, model_config, args):
    prompt = """
    Please first explain the functionality of the python code above. 
    Then generate a possible rewrite for this python code according to your explanation.
    Please organize all the code in a single markdown code block.
    Implemented in golang.
    ```
    {code}
    ```
    """

    if model_config['tokenizer'].pad_token is None:
        model_config['tokenizer'].pad_token = model_config['tokenizer'].eos_token

    pipeline = transformers.pipeline(
        task="text-generation",
        model=model_config['model'],
        tokenizer=model_config['tokenizer']
    )

    rewrite_codes = []
    for code in codes:
        input_prompt = prompt.format(code=code)
        print(code)
        rewritten_code = pipeline(
            input_prompt,
            do_sample=True,
            temperature=0.5,
            top_p=0.95,
            num_return_sequences=1,
            eos_token_id=model_config['tokenizer'].eos_token_id,
            max_length=256,
            truncation=True
        )
        print(878787)
        pattern = r"```(.*?)```"
        rewritten_code = re.findall(pattern, rewritten_code[0], re.DOTALL)
        if rewritten_code:
            rewrite_codes.append(rewritten_code[0].strip())
        else:
            rewrite_codes.append("")
        rewrite_codes.append(rewritten_code[0])
        print(rewritten_code)
        exit()
    return rewrite_codes
