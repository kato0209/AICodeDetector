

class LeapFrogStepState(NamedTuple):
    state: tf.Tensor
    momentum: tf.Tensor
    target_log_prob: tf.Tensor
    target_log_prob_grad: tf.Tensor

class LeapFrogStepExtras(NamedTuple):
    target_log_prob: tf.Tensor
    kinetic_energy: tf.Tensor

FloatTensor = tf.Tensor
PotentialFn = callable

                  step_size: FloatTensor, target_log_prob_fn: PotentialFn,
                  kinetic_energy_fn: Potential