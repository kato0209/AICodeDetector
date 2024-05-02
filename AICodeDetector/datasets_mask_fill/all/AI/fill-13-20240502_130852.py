def remove_word_by_index(text, index):
   words = text.split()
    if 0 <= index < len(words):
       words.pop(index)
    return ' '.join(words)

# 使用例
removed_index_result = remove_word_by_index("Hello world, this is a test sentence.", 1)
