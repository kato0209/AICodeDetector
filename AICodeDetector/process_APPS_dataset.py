import json
import os

with open("APPS_train_path.json") as f:
    fnames = json.load(f)

for fname in fnames:
    question_fname = os.path.join(fname, "question.txt")
    sols_fname = os.path.join(fname, "solutions.json")

    with open(question_fname, 'r') as f:
        question_str = f.read()
    
    with open(sols_fname, 'r') as f:
        sols = json.load(f)
        sol = sols[0]
    
    data = {
        "prompt": question_str,
        "canonical_solution": sol
    }

    with open("APPS_dataset/train.jsonl", 'a') as f:
        json.dump(data, f)
        f.write("\n")

