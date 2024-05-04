def remove_specific_word(text, word_to_remove):
    words = text.split()
    filtered_words = [word for word in <extra_id_0> word != word_to_remove]
  <extra_id_1> return ' '.join(filtered_words)

# 使用例
removed_word_result = remove_specific_word("Hello world, this is a test sentence.", "world,")
