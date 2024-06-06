import transformers
import torch

def load_mask_filling_model(args, mask_filling_model_name, model_config):

    print(f'Loading mask filling model {mask_filling_model_name}...')
    if 'incoder' in mask_filling_model_name:
        mask_model = transformers.AutoModelForCausalLM.from_pretrained(mask_filling_model_name)
    else:
        mask_model = transformers.AutoModelForSeq2SeqLM.from_pretrained(mask_filling_model_name)
    # mask_model.parallelize()
    # to device
    mask_model.to(args.DEVICE)

    try:
        n_positions = mask_model.config.n_positions
    except AttributeError:
        n_positions = 512

    # preproc_tokenizer = transformers.AutoTokenizer.from_pretrained('t5-small', model_max_length=512, cache_dir=model_config['cache_dir'])
    mask_tokenizer = transformers.AutoTokenizer.from_pretrained(mask_filling_model_name, model_max_length=n_positions)
    if 'incoder' in mask_filling_model_name:
        mask_tokenizer.pad_token = "<pad>"
        mask_tokenizer.paddding_side = "left"

    # if args.dataset in ['english', 'german']:
        # preproc_tokenizer = mask_tokenizer

    # model_config['preproc_tokenizer'] = preproc_tokenizer
    model_config['mask_tokenizer'] = mask_tokenizer
    model_config['mask_model'] = mask_model
    return model_config

def load_model(args, model_name, model_config):
    tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
    model = transformers.AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, torch_dtype=torch.float16)
    model.to(args.DEVICE)

    model_config['tokenizer'] = tokenizer
    model_config['model'] = model
    return model_config
