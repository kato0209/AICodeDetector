import tokenize
from io import BytesIO

def tokenize_code(code):
    """ ソースコードをトークン化する """
    tokens = code.split(' ')
    return tokens

def adjust_tokens(tokens, target_length=128):
    """ トークンの数を target_length に調整する """
    if len(tokens) > target_length:
        return tokens[:target_length]
    elif len(tokens) < target_length:
        if not tokens:  # トークンが空の場合の処理
            return ['<empty>'] * target_length  # '<empty>' または他の適当なプレースホルダートークンを使用
        # トークンが足りない場合、最後のトークンを繰り返して追加
        extra_tokens = [tokens[-1]] * (target_length - len(tokens))
        return tokens + extra_tokens
    return tokens

def tokenizer(code):
    # トークン化
    tokens = tokenize_code(code)
    # トークン数の調整
    adjusted_tokens = adjust_tokens(tokens)
    return adjusted_tokens



