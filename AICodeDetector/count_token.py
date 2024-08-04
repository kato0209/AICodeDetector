import tokenize
from io import StringIO

def count_token(code_snippet):

    # Tokenize the code snippet
    tokens = tokenize.generate_tokens(StringIO(code_snippet).readline)

    # Count the number of tokens
    token_count = sum(1 for _ in tokens)

    return token_count
