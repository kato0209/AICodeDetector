

    prior_variables = [
        tf.Variable(initial_value * tf.ones([num_topics]), name='prior_mean'),
        tf.Variable(initial_value * tf.ones([num_topics]), name='prior_stddev')
    ]

        return tfp.distributions.Normal(loc=prior_variables[0], scale=tf.nn.softplus(prior_variables[1]))

    return prior, prior_variables
