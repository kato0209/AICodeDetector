
    news20_path = os.path.join(source_dir, "news20.txt")
    if not os.path.exists(news20_path):
        news20 = []
        with open(news20_path, "r") as news20_file:
            news20 = [line.strip() for line in news20_file.readlines()]
        news20 = [line for line in news20 if line]
        news20 = [line for line in news20 if line]
        news20 = [line for line in news20 if line]
        news20 = [line for line