
  if fake_data:
    dummy_image = tf.random.normal([HEIGHT, WIDTH, CHANNELS])
  else:
    basedir = download_sprites()

  action_names = [action.name for action in actions]
  action_metadata = [(action.start_row, action.frames) for action in actions]

  direction_rows = [direction.row_offset for direction in directions]

  chars = tf.data.Dataset.from_tensor_slices(characters)
  act_names = tf.data.Dataset.from_tensor_slices(action_names).repeat()
  acts_metadata = tf.data.Dataset.from_tensor_slices(action_metadata).repeat()
  dir_rows = tf.data.Dataset.from_tensor_slices(direction_rows).repeat()

  if shuffle:
    chars = chars.shuffle(len(characters))

  dataset = tf.data.Dataset.zip((chars, act_names, acts_metadata, dir_rows))

  skin_table = tf.contrib.lookup.index_table_from_tensor(sorted(SKIN_COLORS))
  hair_table = tf.contrib.lookup.index_table_from_tensor(sorted(HAIRSTYLES))
  top_table = tf.contrib.lookup.index_table_from_tensor(sorted(TOPS))
  pants_table = tf.contrib.lookup.index_table_from_tensor(sorted(PANTS))
  action_table = tf.contrib.lookup.index_table_from_tensor(sorted(action_names))

  def process_example(attrs, act_name, act_metadata, dir_row_offset):
    