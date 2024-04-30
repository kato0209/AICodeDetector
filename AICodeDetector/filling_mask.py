import re

def count_masks(texts):
    # count the number of masks in each text with the pattern "<extra_id_\d+>"
    pattern = re.compile(r"<extra_id_\d+>")
    n_expected = [len(pattern.findall(x)) for x in texts]
    return n_expected


# replace each masked span with a sample from T5 mask_model
def replace_masks(texts, model_config, args):
    n_expected = count_masks(texts)
    stop_id = model_config['mask_tokenizer'].encode(f"<extra_id_{max(n_expected)}>")[0]
    tokens = model_config['mask_tokenizer'](texts, return_tensors="pt", padding=True).to(args.DEVICE)
    # tokens = model_config['mask_tokenizer'](texts, return_tensors="pt", padding=True, return_token_type_ids=False).to(args.DEVICE)
    outputs = model_config['mask_model'].generate(**tokens, max_length=128, do_sample=True, top_p=args.mask_top_p, num_return_sequences=1, eos_token_id=stop_id, temperature=args.mask_temperature)
    return model_config['mask_tokenizer'].batch_decode(outputs, skip_special_tokens=False)
