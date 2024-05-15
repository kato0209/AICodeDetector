

    # Generate sequences
    generated_sequences = []
    for _ in range(samples):
        z = model.sample_prior(batch_size)
        generated_sequence = model.sample_sequence(z, length)
        generated_sequences.append(generated_sequence)

    # Plot original inputs
    fig, axes = plt.subplots(batch_size, length, figsize=(length * 2, batch_size * 2))
    for i in range(batch_size):
        for