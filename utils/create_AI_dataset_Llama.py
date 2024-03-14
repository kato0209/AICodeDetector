from transformers import AutoTokenizer, LlamaForCausalLM
from tqdm import tqdm
import torch
from unsloth import FastLanguageModel
import datetime

# initialize the model
max_seq_length = 2048

model_path = "unsloth/codellama-7b-bnb-4bit"
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#model = LlamaForCausalLM.from_pretrained(model_path, device_map=device)
#tokenizer = AutoTokenizer.from_pretrained(model_path)
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/mistral-7b-bnb-4bit", # Supports Llama, Mistral - replace this!
    max_seq_length = max_seq_length,
    dtype = None,
    load_in_4bit = True,
)

# Do model patching and add fast LoRA weights
model = FastLanguageModel.get_peft_model(
    model,
    r = 16,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0, # Supports any, but = 0 is optimized
    bias = "none",    # Supports any, but = "none" is optimized
    use_gradient_checkpointing = True,
    random_state = 3407,
    max_seq_length = max_seq_length,
)

def remove_code_block_indicator(response):
    # コードブロックインジケーターを削除
    response = response.replace("```", "")
    response = response.replace("```", "")
    return response

def query_Llama_and_save(prompt, file_path, extension):
    tokenizer.pad_token = tokenizer.eos_token
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=4096)

    # Generate
    generate_ids = model.generate(inputs.input_ids.to(device), max_new_tokens=384, do_sample=True, top_p=0.75, top_k=40, temperature=0.1)
    print(generate_ids)
    completion = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    print(completion)
    completion = completion.replace(prompt, "").split("\n\n\n")[0]
    print(completion)

    response_text = remove_code_block_indicator(completion)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{file_path}/{timestamp}.{extension}"
    with open(output_file, 'w') as file:
        file.write(response_text)

    return output_file

# ChatGPTに問い合わせる内容
prompt = """\
Feed-forward neural networks, convolutional neural networks, graph neural networks, Boyer Moore algorithm, Dijkstra algorithm, greatest common division, Levenshtein, logistic regression, matrix multiplication, Rocchio algorithm, SVM

Append text, concatenate file, Excel file,
read file, read file list, write file, copy file,
get modified time, MP3 file

Email, HTTP client/server, FTP client/server, chat client/server

Binary search, exponential search, sequential search, breadth-first search, depth-first
search, linear search, bubble sort, merge sort

Array blocking issue, compare two strings,
delete word, dequeue, common elements,
minimum element

Choose a task at random from the above and implement the code snippet of the chosen task in Golang.
Note: Do not output anything other than the code snippet! """


# レスポンスを保存するファイル名
file_path = "datasets/all/no_label"
extension = "go"


# APIを呼び出してレスポンスを取得し、ファイルに保存
for i in range(1):
    saved_file  = query_Llama_and_save(prompt, file_path, extension)
    print("Response saved to", saved_file )
