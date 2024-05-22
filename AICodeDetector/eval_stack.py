from  datasets  import  load_dataset


# specific language (e.g. Dockerfiles)
ds = load_dataset("bigcode/the-stack", data_dir="data/python", split="test")
for sample in iter(ds): print(sample["content"])
