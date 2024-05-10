
  with ops.name_scope(name, "kl_chi_chi", values=[a.logits, b.logits]):
    # The two distributions can be re-parameterized, so we need to flatten
    # them to put them in the same order as they are added to all.
    a_logits = a.logits + b.logits
    b_logits = b.logits + a.logits
    a_probs = a.probs + b.probs
    b_probs = b.probs + a.probs
    # Compute the batchwise KL(a || b)
    batch_total_probs =