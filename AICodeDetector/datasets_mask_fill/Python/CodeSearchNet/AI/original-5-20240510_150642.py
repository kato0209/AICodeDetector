 before returning them.
    fake_data: Whether to use fake data.

  Returns:
    A tf.data.Dataset with the following fields:
      - character_id: A unique integer ID for each character.
      - action_id: A unique integer ID for each action.
      - action_name: A string representing the action.
      - action_reward: A float representing the reward of the action.
      - action_done: A boolean indicating whether the action has been
        completed.
      - action_reward_mean: A float representing the mean reward of the
        action.
   