def boyer_moore_search(text, pattern):
    # ずらし表の作成
    def build_shift_table(pattern):
        shift_table = {char: len(pattern) for char in set(text)}
        for i in range(len(pattern) - 1):
            shift_table[pattern[i]] = len(pattern) - 1 - i
        return shift_table

    shift_table = build_shift_table(pattern)
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            return i  # パターンが見つかった場合、その位置を返す
        else:
            i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1  # パターンが見つからなかった場合

# 使用例
text = "ここに長いテキストを入れます"
pattern = "テキスト"
result = boyer_moore_search(text, pattern)
print("パターンが見つかった位置:", result)
