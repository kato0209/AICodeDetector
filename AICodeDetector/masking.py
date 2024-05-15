import np
import yake
import random

def yake_code(code):
    language = "en"
    max_ngram_size = 3
    deduplication_threshold = 0.9
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = 128
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(code)

    keyword_list = []
    code_words = set(code.split())  # 元のコードの単語セットを作成
    for kw in keywords:
        if kw[0] in code_words:  # キーワードが元のコード内にあるか確認
            keyword_list.append(kw)
    return keyword_list

# 確率に基づいてワードを選択する関数
def choose_word(words, probabilities):
    # 各ワードの累積確率を計算
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    
    # 0から1までのランダムな値を生成
    rand_value = random.random()

    # ランダムな値がどの範囲に入るかを見つける
    for i, prob in enumerate(cumulative_probabilities):
        if rand_value <= prob:
            return words[i]

def tokenize_and_mask(code, buffer_size=1, span_length=2, pct=0.3, ceil_pct=False, mask_threshold = 0.4):
    probability_list = yake_code(code)
    tokens = code.split()

    mask_string = '<<<mask>>>'

    n_spans = pct * len(tokens) / (span_length + buffer_size * 2)
    if ceil_pct:
        n_spans = np.ceil(n_spans)
    n_spans = int(n_spans)

    if len(probability_list) == 0:
        return code

    n_masks = 0
    while n_masks < n_spans:
        if len(probability_list) == 0:
            break
        words, probabilities = zip(*probability_list)
        selected_word = choose_word(words, probabilities)
        word_found = False
        for idx, token in enumerate(tokens):
            if token == selected_word:
                tokens[idx] = mask_string
                n_masks += 1
                word_found = True
                break
        if not word_found:
            # selected_wordがtokens内にない場合、probability_listから削除
            probability_list = [(word, prob) for word, prob in probability_list if word != selected_word]

    # replace each occurrence of mask_string with <extra_id_NUM>, where NUM increments
    num_filled = 0
    for idx, token in enumerate(tokens):
        if token == mask_string:
            tokens[idx] = f'<extra_id_{num_filled}>'
            num_filled += 1
    assert num_filled == n_masks, f"num_filled {num_filled} != n_masks {n_masks}"
    
    if len(tokens) > 128:
        tokens = tokens[:128]

    text = ' '.join(tokens)
    return text

