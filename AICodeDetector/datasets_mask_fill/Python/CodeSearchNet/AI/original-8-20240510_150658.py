
  with ops.name_scope(name, "kl_deterministic_distribution", values=[a.logits, b.logits]):
    # Calculate the KL(a || b)
    a_ = a.logits
    b_ = b.logits
    # Calculate KL(a)
    kl_a = a_ - b_
    # Calculate KL(b)
    kl_b = b_ - a_
    # Calculate KL(a || b)
    kl_a_minus_b = a_ - b_
    # Calculate KL(a)
    kl_a_minus_b