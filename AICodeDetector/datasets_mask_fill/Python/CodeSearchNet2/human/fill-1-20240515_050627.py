# strategy: # # 
# Creates a model of two variables, each with gradient function
# and variable name -> [variable, grad, adagrad slot] vars_grads = {} for v in tf.trainable_variables(): vars_grads[v.name] = [v, None, None] for g, v in grads: vars_grads[v.name][1] = g vars_grads[v.name][2] = opt.get_slot(v, 'accumulator') # now make summaries #  
# grad_vars[v] = (v, g) for g, v in grads
#  
# varlist = [] for vname, (v, g, a) in vars_grads.items(): if g is None: continue