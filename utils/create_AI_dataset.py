from openai import OpenAI
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

def remove_code_block_indicator(response):
    # コードブロックインジケーターを削除
    response = response.replace("```go", "")
    response = response.replace("```", "")
    return response


def query_chatgpt_and_save(prompt, api_key, file_path, extension, model="gpt-3.5-turbo", temperature=0.7):
    client = OpenAI()
    OpenAI.api_key = api_key

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    response_text = response.choices[0].message.content
    response_text = remove_code_block_indicator(response_text)

    # レスポンスをファイルに保存
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{file_path}/{timestamp}.{extension}"
    with open(output_file, 'w') as file:
        file.write(response_text)

    return output_file

# APIキー（ここにあなたのAPIキーを入れる）
api_key = os.environ['OPENAI_API_KEY']

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
file_path = "datasets/all/AI"
extension = "go"


# APIを呼び出してレスポンスを取得し、ファイルに保存
for i in range(90):
    saved_file  = query_chatgpt_and_save(prompt, api_key, file_path, extension)
    print("Response saved to", saved_file )
