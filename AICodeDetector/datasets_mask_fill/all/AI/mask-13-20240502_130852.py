def remove_word_by_index(text, index):
  <extra_id_0> words = text.split()
    if 0 <= index < len(words):
  <extra_id_1>     words.pop(index)
    return ' '.join(words)

# 使用例
removed_index_result <extra_id_2> world, this is a test sentence.", 1)
