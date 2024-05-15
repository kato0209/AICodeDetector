
  hmc_results = run_hmc(
      num_results=num_results,
      num_burnin_steps=num_burnin_steps,
      num_leapfrog_steps=num_leapfrog_steps,
      step_size=step_size)
  hmc_results = hmc_results[0]
  hmc_results = hmc_results[1:]
  hmc_results = np.array(hmc_results)
  hmc_results = hmc_results.reshape(num_results, -1)
  hmc_results =