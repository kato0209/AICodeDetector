from  datasets  import  load_dataset

# full dataset (3TB of data)
ds = load_dataset("bigcode/the-stack", split="train")

# specific language (e.g. Dockerfiles)
ds = load_dataset("bigcode/the-stack", data_dir="data/python", split="train")

# dataset streaming (will only download the data as needed)
ds = load_dataset("bigcode/the-stack", streaming=True, split="test")
for sample in iter(ds): print(sample["content"])
