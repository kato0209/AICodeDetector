

    config_path = find_config('tfidf_retrieve')
    skill = build_model(config_path)
    agent = EcommerceAgent(skills=[skill])
    return agent