
  # Run HMC on the text-messages.
  hmc_results = run_hmc(
      num_results=num_results,
      num_burnin_steps=num_burnin_steps,
      num_leapfrog_steps=num_leapfrog_steps)
  # Convert to numpy array.
  hmc_results = np.array(hmc_results)
  # Convert to numpy array.
  hmc_results = np.reshape(hmc_results, (num_results, -1))
  # Convert to numpy array.
  hmc_results =